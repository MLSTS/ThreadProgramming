#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
	int A[100];
	int i;
	int psum = 0;
	int sum = 0;
	srand(1234);
	for(i=0;i<100;i++)
		A[i] = rand()%1000;

	#pragma omp parallel private(psum)
	{
		#pragma omp for
		for(i=0;i<100;i++)
			psum = psum + A[i];

		#pragma omp critical
		sum = sum + psum;
	}

for (i=0;i<100;i++)
	printf("A[%d]:%d\n", i, A[i]);
printf("Total sum = %d\n", sum);
}



