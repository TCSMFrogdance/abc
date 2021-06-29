// PARAM

// idslsvg1: string id


function world_map(path1, path2, idsvg){
    var worldMap = d3.select(idsvg);
    worldMap.selectAll('*').remove();
    var width = worldMap.attr('width');
    var height = worldMap.attr('height');
    var projection = d3.geoMercator()        
        .center([0,40]) // GPS of location to zoom on
        .scale(120) // This is like the zoom
        .translate([ width/2, height/2 ]);
    

    d3.queue()
        .defer(d3.json, path1)
        .defer(d3.json, path2)//{% url 'topstores' %}
        .await(render);
    
    function render(error, world, data){
        data.sort(function(b, a) {
            return a.Sales - b.Sales;
        });


        // Data and color scale
        function color_country(i){
            color = ['#004c6d', '#255e7e', '#3d708f', '#5383a1', '#6996b3', '#7faac6', '#94bed9', '#abd2ec', '#c1e7ff', '#d3e8f5', '#e6f4fc','#f2f9fc'];
            return color[i];
        }
        function sale_country(d){
            sales = [4485638.041253188, 4216296.0179977575, 1478576.31726807, 1393897.4990173313, 1270790.101232497, 447345.3790355402, 417371.1928899906, 219006.633798626, 104869.0187075601, 103991.089346264, 75232.530654948, 34625.88008252, 1706.1020538];
            country = ["Germany", "USA", "France", "England", "Sweden", "Canada", "Spain", "Italy", "Switzerland", "Argentina", "Poland", "Norway"];
            for(i=0;i<country.length;i++){
                if (d == country[i]){
                    return sales[i];
                }
            }
            return 0;
        }
        // Draw the map
        worldMap.append("g")
            .selectAll("path")
            .data(world.features)
            .enter()
            .append("path")
                .style("stroke", "black")
                .style("stroke-width", "0.3px")
                .attr("d", d3.geoPath().projection(projection))
                .style("fill", function(d){
                    country = ["Germany", "USA", "France", "England", "Sweden", "Canada", "Spain", "Italy", "Switzerland", "Argentina", "Poland", "Norway"];
                    for(i=0;i<country.length;i++){
                        if (d.properties.name == country[i]){
                            return color_country(i);
                        }
                    }
                    return '#c2d179';
                })
                //tooltips
                .on('mouseover', function(d) {
                    d3.select(this)
                        .style("fill", "#78c679")
                    d3.select("#tooltip")
                        .style("display","inline")
                        .style("left", d3.event.pageX + "px")
                        .style("top", d3.event.pageY + "px")
                        .text(d.properties.name + ' ' + (sale_country(d.properties.name)/1000).toFixed(1) + 'K$' ) ;})
                .on('mouseout', function(){
                    d3.select("#tooltip").style("display", "none"),
                    d3.select(this).style("fill", function(d){
                        country = ["Germany", "USA", "France", "England", "Sweden", "Canada", "Spain", "Italy", "Switzerland", "Argentina", "Poland", "Norway"];
                        for(i=0;i<country.length;i++){
                            if (d.properties.name == country[i]){
                                return color_country(i);
                            }
                        }
                        return '#c2d179';
                    })
                })
                .on('click', function(d){
                    window.open('https://en.wikipedia.org/wiki/' + d.properties.name);
                });
                

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