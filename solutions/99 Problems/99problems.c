#include <stdio.h>

int main(int argc, char *argv[]) {
	int n;
	(void)(scanf("%d", &n)+1);
	
	if (n < 149) {
		printf("99\n");
		return 0;
	}

	int res;
	int rest = n % 100;
	if (rest < 49) {
		res = n - rest - 1;
	} else {
		res = n + (99-rest); 
	}
	printf("%d\n", res);
	return 0;
}
