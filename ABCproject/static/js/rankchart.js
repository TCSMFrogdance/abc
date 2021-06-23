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
    var herRank = d3.select(idsvg);

    var width = +herRank.attr('width');
    var height = +herRank.attr('height');

    herRank.selectAll('*').remove();

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

    var g = herRank.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    var xAxisTickFormat = number =>
        d3.format('.2s')(number)
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
        // .remove();

    xAxisG.select('.domain').remove();

    xAxisG.append('text')
        .attr('class', 'axis-label')
        .attr('y', 65)
        .attr('x', innerWidth / 2)
        .attr('fill', 'black')
        .text(xAxisLabelText);

    g.selectAll('rect')
        .data(data)
        .enter()
        .append('rect')
        .attr('y', d => yScale(yValue(d)))
        .attr('height', yScale.bandwidth())
        .attr("fill", "#69b3a2")
        .on('mouseover', function(d) {
            d3.select(this)
                .attr("stroke", "black", true)
                .attr("stroke-width", "3px")
            d3.select("#tooltip")
                .style("display", "inline")
                .style("left", d3.event.pageX + 20 + "px")
                .style("top", d3.event.pageY + "px")
                .style("display", "inline-block")
                .html((d.Sales/1000000).toFixed(2) + "M $");})
        .on('mouseout', function(){
            d3.select("#tooltip").style("display", "none"),
            d3.select(this).attr("stroke",false)
        })
        

    g.append('text')
        .attr('class', 'title')
        .attr('y', -10) 
        .text(titleText);
    
    g.selectAll("rect")
            .transition()
            .duration(800)
            .attr('width', d => xScale(xValue(d)))
            .delay(function(d,i){return(i*100)})
};

//call render function
let rankChart = path => {
    d3.json(path, data => {
        renderHerRankChart(data);
    });
}