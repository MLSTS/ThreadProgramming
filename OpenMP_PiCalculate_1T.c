#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int num_steps=1000000;
double step, pi;

int main(){
	int i;
	double x, sum = 0.0;
	double st = omp_get_wtime();

	step = 1.0 / (double) num_steps;
	#pragma omp parallel for num_threads(1) private(x) reduction(+:sum)
	for (i = 0; i < num_steps; i++){
		x = (i + 0.5) * step;
		sum = sum + 4.0 / (1.0 + x * x);
	}
	pi = step * sum;
	double et = omp_get_wtime();
	printf("Pi = %.10f\n", pi);
	printf("Execution time: %f second.\n", (et-st));
}
