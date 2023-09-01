import numpy as np
from pyswarms.single import GlobalBestPSO

def sphere(bounds):
    return np.sum(bounds**2)

dimensions = 20
bounds = [(-5, 5) for i in range(dimensions)]

optimizer = GlobalBestPSO(n_particles=50, 
                          dimensions=dimensions, 
                          options={'c1': 0.5, 
                                   'c2': 0.3,
                                   'w': 0.9})

cost, pos = optimizer.optimize(sphere, iters=1000)

print(f"Optimal cost found: {cost}")
print(f"Optimal position: {pos}")
