"""
Defining a set of currents that can be used by other entities in this simulator.
"""
import numpy as np 


class ConstantCurrent:
    def __init__(self, amplitude:float, time:np.ndarray):
        """
        Constant current signal. Amplitude is in this case the value of the Current and 
        time is the period over which it is defined
        """
        self.I0 = None
        self.I = amplitude*np.ones_like(time)
        
    def __str__(self, ) -> str:
        if self.I is None:
            return "Empty _Currents Vector"
        return f"{self.I}"

    def __len__(self, ) -> int:
        return len(self.I)

    def __getitem__(self, i) -> float:
        return self.I[i]
    

class SinusoidalCurrent:
    def __init__(self, amplitude:float, time:np.ndarray) -> None:
        """
        Sinusoidal current signal. Amplitude is the maximum value of the Current and 
        time is the period over which it is defined
        """
        self.I0 = None
        self.I = amplitude*np.sin(time)
        self.time = time 
    def __str__(self, ) -> str:
        r = f"Sinusoidal Current defined between {self.time[0]} and {self.time[-1]} seconds"
        return r


    def __len__(self, ) -> int:
        return len(self.I)

    def __getitem__(self, i) -> float:
        return self.I[i]
    
