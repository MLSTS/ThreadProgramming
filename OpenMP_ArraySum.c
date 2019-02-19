#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
	int A[100];
	int i;
	int sum = 0;
	srand(1234);
	for(i=0;i<100;i++)
		A[i] = rand()%1000;

	#pragma omp parallel for reduction(+:sum)
	for(i=0;i<100;i++)
		sum = sum + A[i];

for (i=0;i<100;i++)
	printf("A[%d]:%d\n", i, A[i]);
printf("Total sum = %d\n", sum);
}



