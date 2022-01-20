# figuro
Simple Python script for generating figures of logic circuits

## Instructions
figure is a quick'n'dirty I wrote to facilitate generating visualizations I use in my personal notes and sketches, so don't expect much of it. There is no input format. Gates are organized in layers, and each layer is a list of lists. Each gate is defined by its type, position and name. The ports are name {gate}\_in1, {gate}\_in2 and {gate}\_out. Each edge is a pair of ports it connects. For any details, refer to the source code.

## Notes
figuro is basically a script that copies images to a canvas, describes ports in graphviz format, and then uses _neato_ for routing. The gates are put _on_ the wires. 

[Issue]: dot doesn't support fixed node positions. neato seams not to support compass ports (i.e. figuro can't choose :e and :w ports to make the result prettier).
