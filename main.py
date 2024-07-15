import numpy as np
import models 
from utils.currents import  ConstantCurrent, SinusoidalCurrent
import matplotlib.pyplot as plt 
import timeit

timeline = np.arange(0, 10, 0.1)
curr = SinusoidalCurrent(amplitude = 10 , time = timeline)

model = models.HodkginHuxley(
    V0 = 0,
    Ek = -12,
    El = 10.6,
    Ena = 120, 

    C = 1,

    gk = 36,
    gl = 120,
    gna = 0.3
) 

import timeit
start = timeit.default_timer()
model.simulate(current_input=curr, time=timeline)
end = timeit.default_timer()
print(end - start)

