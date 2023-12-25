#include <stdio.h>

int main(int argc, char *argv[]) {
	int e, f, c;
	(void)(scanf("%d %d %d", &e, &f, &c)+1);

	int sum=0;
    int bottles = e+f;
    while (bottles >= c) {
        int sodas = bottles/c;
        sum += sodas;
        bottles = bottles%c + sodas;
    }

	printf("%d\n", sum);
	return 0;
}
