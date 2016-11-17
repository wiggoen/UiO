#include <iostream>
#include <fstream>
#include <random>

using namespace std;
ofstream ofile;


// Declaration of functions
double RN();
void MonteCarloSimulation(int N, int mcc);
void moneyExchange();


int main()//int argc, char *argv[])
{
    // Initial conditions
    int N = 500;             // Number of agents
    double m0 = 1000;        // Amount of money at start
    double delta_m = 0.05;   // Typically [0.01, 0.05]
    int transactions = 1e7;  // Number of transactions
    int mcc = 5;             // Monte Carlo cycles ([1e3, 1e4] runs)

    double lambda = 0.25;    // {0.25, 0.5, 0.9}
    // (int or double?) alpha  // [1, 2]

    MonteCarloSimulation(N, mcc);

    return 0;
}


double RN() {
    std::random_device rd;              // Initialize the seed
    std::mt19937_64 gen(rd());          // Call the Mersenne twister random number engine
    std::uniform_real_distribution<double> RandomNumberGenerator(0.0,1.0); // Set up the uniform distribution for x in [0, 1]
    return RandomNumberGenerator(gen);  // Random number
}

void MonteCarloSimulation(int N, int mcc) {
    for (int cycles = 1; cycles <= mcc; cycles++) {
        double epsilon = RN();    // Random number
        int rint = RN()*5;  // Random integer between 0 - 5
        cout << "Random number = " << epsilon << " and random int = " << rint << endl;

        // Find a random pair of agents
        int i = RN()*N;
        int j = RN()*N;
        moneyExchange();

        cout << "i = " << i << "  and  j = " << j << endl;

    }
}

void moneyExchange() {
    double mi_new = epsilon*(mi + mj);
    double mj_new = (1 - epsilon)*(mi + mj);
}
