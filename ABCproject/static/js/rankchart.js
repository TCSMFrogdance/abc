// PARAM
// path: string link api
// title: string
// xlabel: string
// idslsvg: string id
// keylabel: string


// render herizontal rank chart
const renderHerRankChart = data => {
    const titleText = title;
    const xAxisLabelText = xlabel;
    const svg = d3.select(idsvg);

    const width = +svg.attr('width');
    const height = +svg.attr('height');

    svg.selectAll('*').remove();

    data.sort(function(b, a) {
        return a.Sales - b.Sales;
    });

    const xValue = d => d['Sales'];
    const yValue = d => d[keylabel];
    const margin = { top: 30, right: 10, bottom: 40, left: 120 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const xScale = d3.scaleLinear()
        .domain([0, d3.max(data, xValue)])
        .range([0, innerWidth]);

    const yScale = d3.scaleBand()
        .domain(data.map(yValue))
        .range([0, innerHeight])
        .padding(0.1);

    const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const xAxisTickFormat = number =>
        d3.format('.3s')(number)
        .replace('G', 'B');

    const xAxis = d3.axisBottom(xScale)
        .tickFormat(xAxisTickFormat)
        .tickSize(-innerHeight);


    g.append('g')
        .call(d3.axisLeft(yScale))
        .selectAll('.domain, .tick line')
        .remove();

    const xAxisG = g.append('g').call(xAxis)
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