// PARAM
// path: string link api
// title: string
// xlabel: string
// idslsvg: string id
// keylabel: string


// render herizontal rank chart
let renderHerRankChart = data => {
    var titleText = title;
    var xAxisLabelText = xlabel;
    var svg = d3.select(idsvg);

    var width = +svg.attr('width');
    var height = +svg.attr('height');

    svg.selectAll('*').remove();

    data.sort(function(b, a) {
        return a.Sales - b.Sales;
    });

    var xValue = d => d['Sales'];
    var yValue = d => d[keylabel];
    var margin = { top: 30, right: 10, bottom: 40, left: 120 };
    var innerWidth = width - margin.left - margin.right;
    var innerHeight = height - margin.top - margin.bottom;

    var xScale = d3.scaleLinear()
        .domain([0, d3.max(data, xValue)])
        .range([0, innerWidth]);

    var yScale = d3.scaleBand()
        .domain(data.map(yValue))
        .range([0, innerHeight])
        .padding(0.1);

    var g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    var xAxisTickFormat = number =>
        d3.format('.3s')(number)
        .replace('G', 'B');

    var xAxis = d3.axisBottom(xScale)
        .tickFormat(xAxisTickFormat)
        .tickSize(-innerHeight);


    g.append('g')
        .call(d3.axisLeft(yScale))
        .selectAll('.domain, .tick line')
        .remove();

    var xAxisG = g.append('g').call(xAxis)
        .attr('transform', `translate(0,${innerHeight})`)
        .remove();

    xAxisG.select('.domain').remove();

    xAxisG.append('text')
        .attr('class', 'axis-label')
        .attr('y', 65)
        .attr('x', innerWidth / 2)
        .attr('fill', 'black')
        .text(xAxisLabelText);

    g.selectAll('rect').data(data)
        .enter().append('rect')
        .attr('y', d => yScale(yValue(d)))
        .attr('width', d => xScale(xValue(d)))
        .attr('height', yScale.bandwidth())
        .attr("fill", "#69b3a2");
        

    g.append('text')
        .attr('class', 'title')
        .attr('y', -10)
        .text(titleText);
};

//call render function
let rankChart = path => {
    d3.json(path).then(data => {
        renderHerRankChart(data);
    });
}