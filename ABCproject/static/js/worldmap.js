// PARAM

// idslsvg1: string id


function world_map(path1, path2, idsvg){
    var worldMap = d3.select(idsvg);
    worldMap.selectAll('*').remove();
    var width = worldMap.attr('width');
    var height = worldMap.attr('height');
    var projection = d3.geoMercator()        
        .center([0,0]) // GPS of location to zoom on
        .scale(80) // This is like the zoom
        .translate([ width/2, height/2 ]);
    

    d3.queue()
        .defer(d3.json, path1)
        .defer(d3.json, path2)//{% url 'topstores' %}
        .await(render);

    function render(error, sg, data){

        // Draw the map
        worldMap.append("g")
            .selectAll("path")
            .data(sg.features)
            .enter()
            .append("path")
                .style("fill", "#ffffbf")
                .style("stroke", "black")
                .style("stroke-width", "0.3px")
                .attr("d", d3.geoPath().projection(projection))
                //tooltips
                .on('mouseover', function(d) {
                    d3.select(this)
                        .style("fill", "#78c679")
                    d3.select("#tooltip")
                        .style("display","inline")
                        .style("left", d3.event.pageX + "px")
                        .style("top", d3.event.pageY + "px")
                        .text(d.properties.name);})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).style("fill", "#ffffbf")
                })
        //zoom and pan
        var zoom = d3.zoom()
            .scaleExtent([1, 8])
            .on('zoom', function() {
                worldMap.selectAll('g')
                    .attr('transform', d3.event.transform);
                    worldMap.selectAll("circle")
                    .attr('transform', d3.event.transform);
            });
        
        worldMap.call(zoom);
    }
    
}