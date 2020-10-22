import matplotlib.pyplot as plt
import math
import random

def fallingTime(h):
    return math.sqrt(2*h/9.81)

def fallingVel(h):
    return math.sqrt(2*h*9.81)

def simulateFall(h):
    return [h, fallingTime(h), fallingVel(h)]
    
def repeatSimulation(repetition, maxH):
    results = []
    for _ in range(repetition):
        h = random.randint(1, maxH)
        if str(h) not in [hdata[0] for hdata in results]:
            results.append(simulateFall(h))
    print(results)
    return sorted(results)
    
    
fallingData = repeatSimulation(9000, 140000)
print("sorted")
print(fallingData)

plt.plot(
    [result[1] for result in fallingData], 
    [result[0] for result in fallingData]
)
plt.plot(
    [result[2] for result in fallingData],
    [result[0] for result in fallingData]
)
plt.ylabel("Height")
plt.legend[ "Time", "Velocity"])
plt.show()