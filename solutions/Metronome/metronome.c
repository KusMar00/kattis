#include <stdio.h>

int main(int argc, char *argv[]) {
	float n;
	(void)(scanf("%f", &n)+1);
	float res = n/4;
	printf("%.2f", res);
	return 0;
}
