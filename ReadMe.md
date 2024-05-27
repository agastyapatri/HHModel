#   **Simulating the Hodgkin Huxley Neuron**

$$I = C_m \frac{dV_m}{dt} + g_{k}n^4(V_m - V_K$ + g_{Na}m^3h(V_m - V_{Na}) + g_l(V_m - V_l)$

$$\frac{dn}{dt} = \alpha_n(V_m)(1 - n) - \beta_n(V_m)n$$

$$\frac{dm}{dt} = \alpha_m(V_m)(1 - m) - \beta_m(V_m)m$$

$$\frac{dh}{dt} = \alpha_h(V_m)(1 - h) - \beta_h(V_m)h$$

Where 
*   $I$ is the current per unit area $mA/cm^2$

*   $\alpha_i, \beta_i$ are the rate constants for the ith ion channel 

*   $g_i$ is the maximal value of the conductance of the channel 

*   $n, m, h$ are dimensionless probabilities associated with the potassium channel subunit activation. 




