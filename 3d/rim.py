"""
This script defines the rim body.
"""
from math import cos
from math import sin
from math import radians

import cadquery
from Helpers import show

TILE_D = 20
TILE_W = 8.5

BEARING_EXT_D = 6.2
BEARING_EXT_W = 0.6
BEARING_D = 5

PETAL_N = 6
PETAL_D = 4

CENTER_D = 11
GEAR_W = 1

SCREW_D = 2.8
SCREW_W = 1

# Rim body and counterbore
REEL_D0 = TILE_D + 0.5
REEL_H0 = 1

REEL_D1 = TILE_D
REEL_H1 = TILE_W - REEL_H0

rim = cadquery.Workplane('XY')\
    .circle(radius=REEL_D0/2.).extrude(distance=REEL_H0)\
    .faces('>Z').workplane()\
    .circle(radius=REEL_D1/2.).extrude(distance=REEL_H1)\
    .faces('<Z').workplane()\
    .cboreHole(diameter=SCREW_D,
               cboreDiameter=BEARING_EXT_D+0.5,
               cboreDepth=SCREW_W + BEARING_EXT_W)

# Gear
petals_position = CENTER_D / 2.
petals = [(petals_position * sin(radians(i * 360. / PETAL_N)),
           petals_position * cos(radians(i * 360. / PETAL_N)))
          for i in range(PETAL_N)]

aux = rim.faces('>Z').workplane()

rim = aux\
    .pushPoints(petals)\
    .circle(radius=PETAL_D/2).extrude(distance=GEAR_W)

rim = aux\
    .circle(radius=CENTER_D/2).extrude(distance=GEAR_W)\
    .faces('>Z').workplane()\
    .hole(diameter=BEARING_D)

show(rim)
