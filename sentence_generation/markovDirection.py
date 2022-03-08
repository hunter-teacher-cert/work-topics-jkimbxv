import random

#looked up different types of stochastic processes and chose how to naviagate from A to B
#tends to go straight
# if you try to turn then try to undo that turn. Repeating a turn is discouraged due to the path retracing
direction_chain = { #each cardinal direction has a 20% increased chance to repeat itself
    'straight': ['straight','straight','straight', 'left turn', 'right turn'],
    'left turn': ['right turn', 'right turn', 'straight','straight','left turn'],
    'right turn': ['right turn', 'left turn', 'straight','straight','left turn' ]

}

direction = [random.choice(list(direction_chain.keys()))]

for i in range(10):
    direction.append(random.choice(direction_chain[direction[i]]))

print(direction)
