import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 

class Current:
    def __init__(self, amplitude:float, time):
        self.I0 = amplitude
        self.I = amplitude*np.ones_like(time)

    def __repr__(self, ) -> str:
        if self.I is None:
            return "Empty Current Vector"
        return f"{self.I}"

    def __len__(self, ) -> int:
        return len(self.I)

    def __getitem__(self, i) -> float:
        return self.I[i]

if __name__ == "__main__": 
    _time = np.arange(0,10, 0.1)
    I = Current(amplitude=10.0, time=_time)
    print(I[-1])
