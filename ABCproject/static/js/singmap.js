function singapore_map(idsvg1){
    var singMap = d3.select(idsvg1);
    singMap.selectAll('*').remove();
    var width = singMap.attr('width');
    var height = singMap.attr('height');
    var projection = d3.geoMercator()        
        .center([103.85 , 1.32]) // GPS of location to zoom on
        .scale(90000) // This is like the zoom
        .translate([ width/2, height/2 ])
    function drawTooltipStore(d) {

        d3.select("#tooltip")
            .classed("hidden",false)
            .style("left", d3.event.pageX - 50 + "px")
            .style("top", d3.event.pageY - 70 + "px")
            .style("display", "inline-block")
            .html((d.Store) + "<br>" + (d.Sales/1000000).toFixed(2) + "M $");
    }

    d3.queue()
        .defer(d3.json, 'https://raw.githubusercontent.com/TCSMFrogdance/abc/main/singapore_map.json')
        .defer(d3.csv, 'https://raw.githubusercontent.com/TCSMFrogdance/abc/main/app/data/top_store.csv')
        .await(render);

    function render(error, sg, data){

        // Create a color scale
        var allStore = d3.map(data, function(d){return(d.Store)}).keys()
        var color = d3.scaleOrdinal()
            .domain(allStore)
            .range(["gold", "blue", "green", "yellow", "black", "grey", "darkgreen", "pink", "brown"]);
        
        var allRegion = d3.map(data, function(d){return(d.Region)}).keys()

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
                .classed('area', true)
                .attr("d", d3.geoPath().projection(projection))
                .on('mouseover', function(d) {
                    d3.select(this).classed("highlight",true);
                    d3.select("#tooltip")
                        .style("display","inline")
                        .style("left", d3.event.pageX + "px")
                        .style("top", d3.event.pageY + "px")
                        .text(d.properties.PLN_AREA_N);})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).classed("highlight",false)
                });
        
        // Add circles:
        singMap.selectAll("myCircles")
            .data(data)
            .enter()
            .append("circle")
                .attr("cx", function(d){ return projection([d.Longitude, d.Latitude])[0] })
                .attr("cy", function(d){ return projection([d.Longitude, d.Latitude])[1] })
                .attr("r", function(d){ return size(+d.Sales) })
                .style("fill", function(d){ return color(d.Store) })
                .on('mouseover', function(d) {
                    d3.select(this)
                        .attr("stroke", "white", true)
                        .attr("stroke-width", "3px")
                    d3.select("#tooltip")
                        .style("display", "inline")
                        .style("left", d3.event.pageX - 50 + "px")
                        .style("top", d3.event.pageY - 70 + "px")
                        .style("display", "inline-block")
                        .html((d.Store) + "<br>" + (d.Sales/1000000).toFixed(2) + "M $");})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).attr("stroke",false)
                })
                .on('click', function(d){
                    alert((d.Store) + ": " + (d.Sales/1000000).toFixed(2) + "M $");
                });
    }
}