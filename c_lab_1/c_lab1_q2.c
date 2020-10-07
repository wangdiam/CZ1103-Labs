#include <stdio.h>

int main() {
	int total = 0, num = 0, numLines, numCount = 0;
	float average;
	printf("Enter number of lines: \n");
	scanf("%d",&numLines);
	for (int i=0;i<numLines;i++) {
		printf("Enter line %d (end with -1)\n",i+1);
		scanf("%d",&num);
		total += num;
		numCount++;
		while (num != -1) {
			scanf("%d",&num);
			if (num != -1) {
				numCount++;
				total += num;
			}
		}
		printf("Average = %.2f\n",((float)total)/numCount);
		numCount = 0;
		total = 0;
	}
} 
