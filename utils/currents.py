"""
Defining a set of currents that can be used by other entities in this simulator.
"""
import numpy as np 


class Current:
    def __init__(self, amplitude:float, time):
        """
        Defining a base class which is used to define a series of possible current inputs 
        """
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

