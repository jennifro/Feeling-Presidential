var width = 900;
var height = 900;
var radius = 20;

var svg = d3.select("#force").append('svg')
    .attr('width', width)
    .attr('height', height);
    

var simulation = d3.forceSimulation()
    .velocityDecay(0.15)
    .force("link", d3.forceLink().distance(10).id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-100))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collide", d3.forceCollide(function(d) { return d.r + 30; }).strength(0.9).iterations(16))
    .force("x", d3.forceX(0))
    .force("y", d3.forceY(0));

d3.json("/data.json", function(error, graph) {
    if (error) throw error;

    var color = {
        1: 'rgb(9, 33, 64)',
        2: 'rgb(242, 71, 56)',
        3: 'rgb(5, 166, 76)',
        4: 'rgb(2, 73, 89)',
        5: 'rgb(191, 42, 42)' };

    var sizes = {1: 16, 2: 3, 3: 5, 4: 5, 5: 5 };

    var cirColor = {
        1: 'rgb(9, 33, 64)',
        2: 'rgb(242, 71, 56',
        3: 'rgb(5, 166, 76)',
        4: 'rgb(2, 73, 89)',
        5: 'rgb(191, 42, 42)' };

    var fontSize = {
        1: 20,
        2: 12,
        3: 14,
        4: 14,
        5: 14 };

    var linkWidth = {
        "prez-speech": 2,
        "speech-bigram": 1.5
    };

    var linkColor = {
        "prez-speech": 'rgb(9, 33, 64)',
        "speech-bigram": 'rgb(242, 71, 56)'
    };

    var link = svg.append("g").selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("class", function(d) { return "link " + d.type; })
        .style('stroke-width', function(d) { return linkWidth[d.type]; })
        .style("stroke", function(d) { return linkColor[d.type]; });
      // .attr("stroke-width", '1px');

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("r", function(d) { return sizes[d.group]; })
        .attr("fill", function(d) { return cirColor[d.group]; })
        .attr('class', function(d) { return 'node' + d.group; })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("title")
        .text(function(d) { return d.id; });
  
    var text = svg.append("g").selectAll("text")
        .data(graph.nodes)
        .enter().append("text")
        .attr("dx", 5)
        .attr("dy", ".31em")
        .attr('text-anchor', 'start')
        .text(function(d) { return d.name; })
        .attr('class', function(d) { return 'text' + d.group; })
        .style('fill', function(d) { return color[d.group]; })
        .style('font-size', function(d) { return fontSize[d.group]; });

    // node.append("image")
    //  .attr("xlink:href", function(d) { return d.icon; })
    //   .attr("x", "-12px")
    //   .attr("y", "-12px")
    //   .attr("width", "24px")
    //   .attr("height", "24px");

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);


    function ticked() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
            .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

        text
            .attr("x", function (d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
            .attr("y", function (d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

         // node.each(collide(0.5));
    }

});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}