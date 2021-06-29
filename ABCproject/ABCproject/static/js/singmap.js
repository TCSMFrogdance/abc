// PARAM

// idslsvg1: string id


function singapore_map(path1, path2, idsvg){
    var singMap = d3.select(idsvg);
    singMap.selectAll('*').remove();
    var width = singMap.attr('width');
    var height = singMap.attr('height');
    var projection = d3.geoMercator()        
        .center([103.85 , 1.32]) // GPS of location to zoom on
        .scale(90000) // This is like the zoom
        .translate([ width/2, height/2 ]);
    

    d3.queue()
        .defer(d3.json, path1)
        .defer(d3.json, path2)//{% url 'topstores' %}
        .await(render);

    function render(error, sg, data){

        // Create a color scale
        var allStore = d3.map(data, function(d){return(d.Store)}).keys()
        var color_store = d3.scaleOrdinal()
            .domain(allStore)
            .range(["gold", "blue", "green", "peru", "olive", "grey", "coral", "pink", "darkorchid"]);
        
        // var allRegion = d3.map(data, function(d){return(d.Region)}).keys()
        // var color_region = d3.scaleOrdinal()
        //     .domain(allRegion)
        //     .range(["#2fcef8", "#d40000", "#ffcc00", "#5cbd54", "#fa6500"]);

        // Add a scale for bubble size
        var valueExtent = d3.extent(data, function(d) { return +d.Sales; })
        var size = d3.scaleSqrt()
            .domain(valueExtent)  // What's in the data
            .range([10, 25])  // Size in pixel
        // Draw the map
        singMap.append("g")
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
                        .text(d.properties.PLN_AREA_N);})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).style("fill", "#ffffbf")
                })
                .on('click', function(d){
                    window.open('https://www.google.com//search?q=singapore ' + d.properties.PLN_AREA_N);
                });

        
        // Add circles:
        singMap.selectAll("myCircles")
            .data(data)
            .enter()
            .append("circle")
                .attr("cx", function(d){ return projection([d.Longitude, d.Latitude])[0] })
                .attr("cy", function(d){ return projection([d.Longitude, d.Latitude])[1] })
                .attr("r", function(d){ return size(+d.Sales) })
                .style("fill", function(d){ return color_store(d.Store) })
                //tooltips
                .on('mouseover', function(d) {
                    d3.select(this)
                        .attr("r", function(d){ return size(+d.Sales) +10 })
                    d3.select("#tooltip")
                        .style("display", "inline")
                        .style("left", d3.event.pageX - 50 + "px")
                        .style("top", d3.event.pageY - 70 + "px")
                        .style("display", "inline-block")
                        .html((d.Store) + "<br>" + (d.Sales/1000000).toFixed(2) + "M $");})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).attr("r", function(d){ return size(+d.Sales)})
                })
                .on('click', function(d){
                    window.open('https://www.google.com//search?q=singapore ' + d.Store);
                });
        //zoom and pan
        var zoom = d3.zoom()
            .scaleExtent([1, 8])
            .on('zoom', function() {
                singMap.selectAll('g')
                    .attr('transform', d3.event.transform);
                singMap.selectAll("circle")
                    .attr('transform', d3.event.transform);
            });
        
        singMap.call(zoom);
    }
}