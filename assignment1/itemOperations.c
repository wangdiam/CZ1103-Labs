#include <stdio.h>
#include <limits.h>
#define MAX 10
void initialize(int *size, int ar[]);
void insert(int max, int *size, int ar[], int num);
void iremove(int *size, int ar[], int num);
void display(int size, int ar[]);
int main()
{
   int  option = 0;
   int  num, ar[MAX], size = 0;
 
   printf("Please select an option: \n");
   printf("(1) Initialize the array \n");
   printf("(2) Insert an integer \n");
   printf("(3) Remove an integer \n");
   printf("(4) Display the numbers stored in the array \n");
   printf("(5) Quit \n");
   do {
      printf("Enter your choice: \n");
      scanf("%d", &option);
      switch (option) {
         case 1:
            initialize(&size, ar);
            break;            
         case 2:
            printf("Enter an integer: \n");
            scanf("%d", &num);
            insert(MAX, &size, ar, num);
            break;            
         case 3:
            printf("Enter the integer to be removed: \n");
            scanf("%d", &num);
            iremove(&size, ar, num);
            break;          
         case 4:
            display(size, ar);
            break;         
         default:
            break;
      }         
   } while (option < 5);
   return 0;
}
void display(int size, int ar[]) 
{
   int i;
   
   printf("The %d numbers in the array: \n", size);
   for(i = 0; i < size; i++) 
      printf("%d ", ar[i]);
   printf("\n");
   
}
void initialize(int *size, int ar[]) 
{
	/*edit*/
   	/* Write your code here */
   	printf("Enter the total number of integers (MAX=10):\n");
	scanf("%d",size);
	printf("Enter the integers:\n");
	for (int i=0;i<*size;i++) {
		scanf("%d",&ar[i]);
	}
	for (int i=1;i<*size;i++) {
		for (int j=0;j<*size-1;j++) {
			if (ar[j] > ar[i]) {
				int temp = ar[j];
				ar[j] = ar[i];
				ar[i] = temp;
			}
		}
	}
	/*end_edit*/
}
void insert(int max, int *size, int ar[], int num) 
{
	/*edit*/
   	/* Write your code here */
	if (*size == max) {
		printf("The array is full\n");
		return;
	}
	*size += 1;
	ar[max-1] = num;
	for (int i=1;i<*size;i++) {
		for (int j=0;j<*size-1;j++) {
			if (ar[j] > ar[i]) {
				int temp = ar[j];
				ar[j] = ar[i];
				ar[i] = temp;
			}
		}
	}
	/*end_edit*/
}
void iremove(int *size, int ar[], int num) 
{
	/*edit*/
   	/* Write your code here */
	for (int i=0;i<*size;i++) {
		if (ar[i] == num) {
			ar[i] = INT_MAX;
			for (int i=1;i<*size;i++) {
				for (int j=0;j<*size-1;j++) {
					if (ar[j] > ar[i]) {
						int temp = ar[j];
						ar[j] = ar[i];
						ar[i] = temp;
					}
				}
			}
			*size -= 1;
			printf("The integer is removed\n");
			return;
		}
	}	
	if (*size == 0) {
		printf("The array is empty\n");
	} else {
		printf("The number is not in the array\n");
	}
	return;
	/*end_edit*/
}
