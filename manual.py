import numpy as np
import random

snowball= np.array([1,1.45,0.52,0.72])
pizza = np.array([0.7, 1, 0.31, 0.48])
nugget = np.array([1.95, 3.1, 1, 1.49])
seashell = np.array([1.34, 1.98, 0.64, 1])

exchanges = [snowball, pizza, nugget, seashell]

res = {}

for i in range(10000):
    market = 3
    total = 500
    path = [3]
    for i in range(4):
        trade = random.randint(0,3)
        total *= exchanges[market][trade]
        market = trade
        path.append(market)
    
    total *= exchanges[market][3]
    path.append(3)

    res[tuple(path)] = total

top_3 = sorted(res.items(), key=lambda item: item[1], reverse=True)[:3]

for key, value in top_3:
    print(f"{key}: {value}")
