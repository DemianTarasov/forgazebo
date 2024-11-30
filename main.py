import xml.etree.ElementTree as ET
import random

tree = ET.parse('clover_aruco.world')
world = tree.getroot()

colors = ['model://dronepoint_yellow/meshes/dronepoint.dae',
          'model://dronepoint_red/meshes/dronepoint.dae',
          'model://dronepoint_green/meshes/dronepoint.dae',
          'model://dronepoint_blue/meshes/dronepoint.dae']
poss = [(1.2, 1.2), (3.4, 1.2), (5.6, 1.2), (7.8, 1.2),
        (1.2, 3.4), (3.4, 3.4), (5.6, 3.4), (7.8, 3.4),
        (1.2, 5.6), (3.4, 5.6), (5.6, 5.6), (7.8, 5.6),
        (1.2, 7.8), (3.4, 7.8), (5.6, 7.8), (7.8, 7.8)]
for i in range(3, 8):
  randomColor = colors[random.randrange(4)]
  randomPos = poss[random.randrange(len(poss))]
  poss.remove(randomPos)
  
  world[0][i][1][0][1][0][0].text = randomColor
  world[0][i][1][1][1][0][0].text = randomColor
  world[0][i][2].text = f'{randomPos[0]} {randomPos[1]} 1 0 0 0'
  

tree.write('clover_aruco.world')
