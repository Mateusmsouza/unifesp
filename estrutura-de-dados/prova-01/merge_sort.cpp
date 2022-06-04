#include<iostream>
using namespace std;

void merge(int arr[], int p, int q, int r) {
    int i, j, k;

   int arr_aux[r-p+1];

   for(i = p; i <= q; i++) arr_aux[i - p] = arr[i];
   for(j = q + 1; j <= r; j++) arr_aux[r + q + 1 - j - p] = arr[j];

    i = p;
    j = r;
    for (k = p; k <= r; k++){
        if (arr_aux[i - p] <= arr_aux[j - p]) {
            arr[k] = arr_aux[i - p];
            i = i + 1;
        }
        else {
            arr[k] = arr_aux[j - p];
            j = j - 1;
        
        }
    }
        
}

void mergeSort(int arr[], int l, int r) {
   int m;
   if(l < r) {
      int m = l+(r-l)/2;

      mergeSort(arr, l, m);
      mergeSort(arr, m+1, r);
      merge(arr, l, m, r);
   }
}

void print(int arr[], int n) {
   for(int i = 0; i < n; i++)
      cout << arr[i] << " ";
   cout << endl;
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6 };
	int n = sizeof(arr) / sizeof(arr[0]);

	mergeSort(arr, 0, n);
	print(arr, n);
}
