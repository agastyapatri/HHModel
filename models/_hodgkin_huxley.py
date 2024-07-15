import numpy as np 

class HodkginHuxley:
    def __init__(
            self, 
            V0:float, 
            Ek:float,
            Ena:float,
            El:float,
            
            C:float,
            gna:float, 
            gk:float,
            gl:float 
        ) -> None:
        """
        Defining the Hodkgin Huxley Model of action potentials

        Note that all the voltages are in mV 
        

        default values for the arguments are:
            V0 = 0,
            Ek = -12,
            El = 10.6,
            Ena = 120
        
        default values for the maximal conductances are, in mS/cm**2j:

            gk = 36,
            gl = 120,
            gna = 0.3


        default value for the capacitance isin micro Farads:

            C = 1
        """
        self.V0 = V0
        self.Ek = Ek
        self.Ena = Ena
        self.El = El

    def alpha_m(self, ) -> float:
        return 0.1*(25-self.V0)/(np.exp(2.5 - 0.1*self.V0) - 1)    
    
    def alpha_h(self, ) -> float:
        return 0.07*np.exp(-0.05*self.V0)
    
    def alpha_n(self, ) -> float:
        return 0.1*(10-self.V0)/(np.exp(1 - 0.1*self.V0) - 1)    
    
    def beta_m(self, ) -> float:
        return 4*np.exp(-self.V0/18)
    
    def beta_h(self, ) -> float:
        return 1/(np.exp(3 - 0.1*self.V0) +1)
    
    def beta_n(self, ) -> float:
        return 0.125 * np.exp(-self.V0/80)
    
    def simulate(self, current_input:np.ndarray, time:np.ndarray) -> np.ndarray:
        """
        the initial state of the model is of the form [V, m, h, n]
        the solutions returned are of the same form 
        """
        _init_state = np.array([0, 0, 0, 0])
        solution_matrix = np.zeros((4, time.shape[-1]))

        

        return solution_matrix





    #--------------------------------------------------------------------#
    # class information#
    #--------------------------------------------------------------------#
    def __str__(self, ) -> str:
        return "The Hodkgin huxley model of action potentials"
    

