/*      
 *      Simulating the Hodkgin Huxley Model, stimulated by a specific current input
 */
#include <stdio.h>
#include <math.h>
#include "currents.h"
#include "neuron.h"
int main(){
    Neuron neuron;
    neuron.V_Na = 0.5;
    neuron.V_L = 1.0;
    neuron.V_K = 1.5;

    printf("%f\n", dV(neuron.V_L, neuron.V_Na));
    
}

