import random

#looked up different types of stochastic processes and chose brownian motion

brownian_chain = { #each cardinal direction has a 20% increased chance to repeat itself
    'N': ['N', 'N', 'S', 'E', 'W'],
    'S': ['N', 'S', 'S', 'E', 'W'],
    'E': ['N', 'S', 'E', 'E', 'W'],
    'W': ['N', 'S', 'E', 'W', 'W'],
}

direction = [random.choice(list(brownian_chain.keys()))]

for i in range(10):
    direction.append(random.choice(brownian_chain[direction[i]]))

print(direction)
