#include "rateconstants.hpp"
#include <cmath>

/*NOTE THAT IN THE FOLLOWING FUNCTIONS; V = V_memrane  - V_rest*/

double alpha_n(double V){
	return (0.01*(10 - V))/(exp((10-V)/(10)) - 1);
}
double alpha_h(double V){
	return 0.07*exp(-0.05*V);
}
double alpha_m(double V){
	return (2.5 - 0.1*V)/(exp(2.5 - 0.1*V) - 1);
}


double beta_n(double V){
	return 0.125 * exp(-(V / 80));
}
double beta_h(double V){
	return 1 / (exp(3 - 0.1*V) + 1);
}
double beta_m(double V){
	return 4*exp(-(V / 18));
}

