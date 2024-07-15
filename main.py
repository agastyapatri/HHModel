import numpy as np
import models 
from utils.currents import  ConstantCurrent, SinusoidalCurrent
import matplotlib.pyplot as plt 
import timeit

timeline =np.linspace(0, 10, 100) 
start = timeit.default_timer()
curr = SinusoidalCurrent(amplitude = 10 , time = timeline)
end = timeit.default_timer()
print(end - start)

plt.plot(timeline, curr)
plt.show()
