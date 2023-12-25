#include <stdio.h>

int main() {
	int n;
	(void)(scanf("%d", &n)+1);
	if (n%2 == 0) {
		printf("second\n");
	} else {
		printf("first\n");
	}
	return 0;
}
