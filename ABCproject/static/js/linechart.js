// PARAM

// idsvg1: string id
// path1: string link api
// title1: string

function line(path, idsvg, title){
    d3.json(path, function(data) {
        renderLineChart(data);
    });
    
    function renderLineChart(data){
        var linechart = d3.select(idsvg);

        var width = linechart.attr('width');
        var height = linechart.attr('height');
        var margin = {top: 10, right: 10, bottom: 10, left: 10},
        width = width - margin.left - margin.right,
        height = height - margin.top - margin.bottom;

        linechart.selectAll('*').remove();

        linechart.append('text')
            .attr('class', 'title')
            .attr('x', 50)
            .attr('y', 20) 
            .text(title)
            .style("font-size", "15px")
            .attr("alignment-baseline","middle");
        var sumstat = d3.nest() 
            .key(function(d) { return d.year;})
            .entries(data);

        var x = d3.scaleLinear()
            .domain(d3.extent(data, function(d) { return d.month; }))
            .range([ 30, width ]);

        linechart.append("g").attr("id", "axis")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).ticks(12));

        var y = d3.scaleLinear()
            .domain([0, d3.max(data, function(d) { return +d.Sales; })])
            .range([ height, 30 ]);
        
        var res = sumstat.map(function(d){ return d.key }) 

        var color = d3.scaleOrdinal()
            .domain(res)
            .range(['#e41a1c','#377eb8','#4daf4a'])
        
        
        linechart.append("g").attr("id", "line")
            .selectAll(".line")
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

        linechart.append("g").attr("id", "legend")
            .selectAll('year')
            .data(sumstat)
            .enter()
            .append('circle')
                .attr("cx", width - 80 )
                .attr("cy", function(d) { return 20 + (d.key - 2015)*20 } )
                .attr("r", 6)
                .attr("fill", function(d){ return color(d.key) })

        linechart.append("g").attr("id", "textlegend")
            .selectAll('labelLegend')
            .data(sumstat)
            .enter()
            .append('text')
                .attr("x", width - 70 )
                .attr("y", function(d) { return 20 + (d.key - 2015)*20 } )
                .text(function(d){ return d.key + ":" })
                .style("font-size", "15px")
                .attr("alignment-baseline","middle")


        function get_data(month){
            list = [];
            for(i = 0; i < data.length; i++){
                if(data[i].month == month){
                    list.push(data[i]);
                }
            }
            return list;
        }
        linechart.append("g").attr("id", "circle")
            .selectAll('datapoint')
            .data(data)
            .enter()
            .append('circle')
                .attr("cx", function(d) { return x(d.month) } )
                .attr("cy", function(d) { return y(d.Sales) } )
                .attr("r", 3)
                .attr("fill", "white")
                .attr("stroke", function(d){ return color(d.year) })
            .on('mouseover', function(d){
                // console.log(d3.event.pageX, d3.event.pageY);
                linechart.append("g").attr("id", "highlight")
                    .selectAll('dot')
                    .data(get_data(d.month))
                    .enter()    
                    .append('circle')
                        .attr("cx", function(d) { return x(d.month) } )
                        .attr("cy", function(d) { return y(d.Sales) } )
                        .attr("r", 6)
                        .attr("fill", "white")
                        .attr("stroke", function(d){ return color(d.year) })                          
                linechart.append("g").attr("id", "hover")
                    .selectAll('hoverText')
                    .data(get_data(d.month))
                    .enter()
                    .append('text')
                        .attr("x", function(d) { return (width - 35) } )
                        .attr("y", function(d) { return 20 + (d.year - 2015)*20 } )
                        .text(function(d){ return ((d.Sales/1000).toFixed(0) + "K$") })
                        .style("font-size", "15px")
                        .attr("alignment-baseline","middle")
                })
            .on('mouseout', function(){
                d3.selectAll("#hover").remove()
                d3.selectAll('#highlight').remove();
            })
    }
}
