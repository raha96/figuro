from PIL import Image
import subprocess

gates = {
    "and": Image.open("gates/and.png"), 
    "nand": Image.open("gates/nand.png"), 
    "or": Image.open("gates/or.png"), 
    "nor": Image.open("gates/nor.png"), 
    "xor": Image.open("gates/xor.png"), 
    "xnor": Image.open("gates/xnor.png"), 
    "not": Image.open("gates/not.png")
}

def addT (t1, t2):
    return (t1[0]+t2[0] , t1[1]+t2[1])

def putLayers (canvas:Image.Image, layers, offset=(22,0)):
    for layer in layers:
        for gate, pos, name in layer:
            canvas.paste(gate, addT(pos,offset), gate)

def genDot (canvas:Image.Image, layers, edges):
    size = canvas.size
    output  = 'graph "logic" {\n'
    output += '    graph [dpi=300 inputscale=300 splines=ortho];\n'
    output += '    node [shape=point];\n'
    for layer in layers:
        for gate, pos, name in layer:
            np = size[1]-pos[1]
            output += f'    {name}_in1 [pos="{pos[0]},{np-31}!"];\n'
            output += f'    {name}_in2 [pos="{pos[0]},{np-128}!"];\n'
            output += f'    {name}_out [pos="{pos[0]+260},{np-80}!"];\n'
    for edge in edges:
        output += f'    {edge[0]} -- {edge[1]};'
    output += '}\n'
    return output

layer1 = [
    [gates['and'], (0,0), 'g1'], 
    [gates['or'], (0,160), 'g2']
]
layer2 = [
    [gates['and'], (520,0), 'g3'], 
    [gates['or'], (520,160), 'g4']
]
layers = [layer1, layer2]

edges = [
    ('g1_out', 'g3_in1'), 
    ('g1_out', 'g4_in1'), 
    ('g2_out', 'g3_in2'), 
    ('g2_out', 'g4_in2')
]

size = (1024, 680)
canvas = Image.new ('RGBA', size, color=(255,255,255,0))
#canvas.show()
outputPath = 'test.gv'
outFile = open(outputPath, 'w')
outFile.write (genDot(canvas, layers, edges))
outFile.close()

subprocess.run(["neato", "-Tpng", outputPath, "-o", "test.png"])

connections = Image.open("test.png").convert('RGBA')
canvas.paste(connections, (0,5), connections)
putLayers(canvas, layers)

canvas.show()