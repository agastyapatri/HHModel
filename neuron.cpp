#include <cmath>
#include <iostream>
#include <vector>
#include <cmath>


typedef std::vector<float> vfloat;



class Current{
public:
	double omega;
	double time;
	int num_steps;
	double amplitude;
};


int main(){
	Current I;
	I.omega = 0.1;
	I.time = 10;
	I.num_steps = 100;
	I.amplitude = 10;
}
