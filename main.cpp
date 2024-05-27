#include <iostream>
#include "include/rateconstants.hpp"

int main(){
	double V = 0.0;
	std::cout << alpha_h(V) << std::endl;
	std::cout << alpha_m(V) << std::endl;
	std::cout << alpha_n(V) << std::endl;

	std::cout << beta_h(V) << std::endl;
	std::cout << beta_m(V) << std::endl;
	std::cout << beta_n(V) << std::endl;
}

