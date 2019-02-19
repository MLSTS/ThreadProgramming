#include <stdio.h>
#include <stdlib.h>

int main(){
	int A[100];
	int B[100];
	int i;
	srand(1234);
	for(i=0;i<100;i++)
		A[i] = rand()%1000;

	for(i=0;i<100;i++)
		B[i] = A[i]*10;

for (i=0;i<100;i++)
	printf("[%d]: A = %d | B = %d\n", i, A[i], B[i]);
}


