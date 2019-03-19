#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
    int x, n = 10;
	int a[n], b[n];
	int i, j;
	srand(1234);
	for(i = 0 ; i < n ; i++)
		a[i] = rand()%1000;

    #pragma omp parallel for
    for (i = 0; i < n; i++) { /* for each number */
        x = 0;
        for (j = 0; j < n; j++) /* count number less than it */
            if ((a[i] > a[j]) || (a[i] == a[j]) && (j <i))
                x++;
        b[x] = a[i]; /* copy number into correct place */
    }

for (i = 0; i < n ; i++)
	printf("A[%d]:%d\n", i, a[i]);
for (i = 0; i < n ; i++)
    printf("B[%d]:%d\n", i, b[i]);
}