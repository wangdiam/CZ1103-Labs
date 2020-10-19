#include <stdio.h>
#define SIZE 10
#define INIT_VALUE 999
int symmetry2D(int M[][SIZE], int rowSize, int colSize);
int main() 
{
   int M[SIZE][SIZE],i,j, result = INIT_VALUE;
   int rowSize, colSize;
   
   printf("Enter the array size (rowSize, colSize): \n");
   scanf("%d %d", &rowSize, &colSize); 
   printf("Enter the matrix (%dx%d): \n", rowSize, colSize);
   for (i=0; i<rowSize; i++)
      for (j=0; j<colSize; j++)
         scanf("%d", &M[i][j]);    
   result=symmetry2D(M, rowSize, colSize);
   if (result == 1)
      printf("symmetry2D(): Yes\n");
   else if (result == 0)
      printf("symmetry2D(): No\n"); 
   else
      printf("Error\n");
   return 0;
}
int symmetry2D(int M[][SIZE], int rowSize, int colSize) 
{
	/*edit*/
   	/* Write your code here */
	if (rowSize != colSize) return 0;
	int arr[colSize][rowSize];
	for (int i=0;i<rowSize;i++) {
		for (int j=0;j<colSize;j++) {
			arr[j][i] = M[i][j];
		}
	}
	for (int i=0;i<rowSize;i++) {
		for (int j=0;j<colSize;j++) {
			if (arr[i][j] != M[i][j]) return 0;
		}
	}
	return 1;
	/*end_edit*/
}
