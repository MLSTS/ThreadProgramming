#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
	int A[100];
	int i;
	int max = 0;
	srand(1234);
	for(i=0;i<100;i++)
		A[i] = rand()%1000;

	#pragma omp parallel for reduction(max:max)
	for(i=0;i<100;i++)
		if(A[i] > max)
			max = A[i];

for (i=0;i<100;i++)
	printf("A[%d]:%d\n", i, A[i]);
printf("Maximum value = %d\n", max);
}



