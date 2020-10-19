#include <stdio.h>
void printPattern3(int height);
int main()
{
   int height;

   printf("Enter the height: \n");
   scanf("%d", &height);
   printf("printPattern3(): \n");
   printPattern3(height);
   return 0;
}
void printPattern3(int height)
{        
	/*edit*/
   /* Write your code here */
   int j=1;
	for (int i=1;i<height+1;i++) {
		for (int k=0;k<i;k++) {
			printf("%d ",j);
			j++;
			if (j>9) j=0;
		}
		j=i+1;
		printf("\n");
	}

	/*end_edit*/
}
