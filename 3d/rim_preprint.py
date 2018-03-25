"""
This script defines the rim body.
"""
from math import cos
from math import sin
from math import radians

import cadquery
from Helpers import show

TOLERANCE = 0.2

TILE_D = 20
TILE_W = 8.5

BEARING_EXT_D = 6.2
BEARING_EXT_W = 0.6
BEARING_D = 5 + TOLERANCE

PETAL_N = 6
PETAL_D = 3.8 - TOLERANCE
PETAL_CENTER = 11

CENTER_D = 9
GEAR_W = 1

SCREW_D = 2.8
SCREW_W = 1

# Rim body and counterbore
REEL_D1 = TILE_D
REEL_H1 = TILE_W - (SCREW_W+BEARING_EXT_W)

rim = cadquery.Workplane('XY')\
    .circle(radius=REEL_D1/2.).extrude(distance=REEL_H1)\

# Gear
petals_position = PETAL_CENTER / 2.
petals = [(petals_position * sin(radians(i * 360. / PETAL_N)),
           petals_position * cos(radians(i * 360. / PETAL_N)))
          for i in range(PETAL_N)]

aux = rim.faces('>Z').workplane()

rim = aux\
    .pushPoints(petals)\
    .circle(radius=PETAL_D/2.).extrude(distance=GEAR_W)

rim = aux\
    .circle(radius=CENTER_D/2.).extrude(distance=GEAR_W)\
    .edges("|Z").fillet(0.5)\
    .faces('>Z').workplane()\
    .hole(diameter=BEARING_D)

show(rim)
