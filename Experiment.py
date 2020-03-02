LEFT =       {NORTH: WEST,
                   SOUTH: EAST,
                   EAST:  NORTH,
                   WEST:  SOUTH,
                   STOP:  STOP}

RIGHT =      dict([(y,x) for x, y in LEFT.items()])
print (RIGHT)