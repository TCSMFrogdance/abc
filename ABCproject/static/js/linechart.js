// PARAM

// idslsvg1: string id

function line(idslsvg1){
    var linechart = d3.select(idsvg1);
    linechart.selectAll('*').remove();
    var width = linechart.attr('width');
    var height = linechart.attr('height');
    var margin = {top: 10, right: 10, bottom: 10, left: 10},
    width = width - margin.left - margin.right,
    height = height - margin.top - margin.bottom;

    d3.json("https://raw.githubusercontent.com/TCSMFrogdance/abc/main/app/data/saleByMonth_Year.json", function(data) {
        
        var sumstat = d3.nest() 
            .key(function(d) { return d.year;})
            .entries(data);
    
        var x = d3.scaleLinear()
            .domain(d3.extent(data, function(d) { return d.month; }))
            .range([ 0, width ]);
        linechart.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).ticks(12));

        var y = d3.scaleLinear()
            .domain([0, d3.max(data, function(d) { return +d.Sales; })])
            .range([ height, 0 ]);
        
        var res = sumstat.map(function(d){ return d.key }) 

        var color = d3.scaleOrdinal()
            .domain(res)
            .range(['#e41a1c','#377eb8','#4daf4a'])
        
        
        linechart.selectAll('verline')
            .data(data)
            .enter()
            .append('rect')
                .style("fill", "white")
                .attr('x', d => x(d.month))
                .attr("width", "1px")
                .attr("height",  height )
            .on('mouseover', function(){
                d3.select(this).style("stroke", "black").attr("stroke-width", "2px");
            })
            .on('mouseout', function(){
                d3.select(this).style("stroke", "none");
            })

        linechart.selectAll(".line")
            .data(sumstat)
            .enter()
            .append("path")
            .attr("fill", "none")
            .attr("stroke", function(d){ return color(d.key) })
            .attr("stroke-width", 1.5)
            .attr("d", function(d){
                return d3.line()
                .x(function(d) { return x(d.month); })
                .y(function(d) { return y(d.Sales); })
                (d.values)
            })
        
        linechart.selectAll('datapoint')
            .data(data)
            .enter()
            .append('circle')
                .attr("cx", function(d) { return x(d.month) } )
                .attr("cy", function(d) { return y(d.Sales) } )
                .attr("r", 1)
                .attr("fill", "white")
                .attr("stroke", function(d){ return color(d.year) })
            .on('mouseover', function(d){
                d3.select(this)
                    .attr("r", 6)
                    .attr("stroke-width", "2px")
                d3.select("#tooltip")
                    .style("display", "inline")
                    .style("left", d3.event.pageX + 20 + "px")
                    .style("top", d3.event.pageY + "px")
                    .style("display", "inline-block")
                    .html((d.Sales/1000).toFixed(2) + "K $");
                })
            .on('mouseout', function(){
                d3.select("#tooltip").style("display", "none"),
                d3.select(this).attr("r", 1);
            })

        linechart.on('mouseover', function(){
            console.log(d3.event.pageX, d3.event.pageY);
        })

            
        
    })
}
