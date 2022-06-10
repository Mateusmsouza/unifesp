#include<iostream>
using namespace std;

int num_comparisions_merge = 0;
int num_changes_merge = 0;

void merge(int arr[], int p, int q, int r) {
    int i, j, k;

   int arr_aux[r-p+1];

   for(i = p; i <= q; i++){
       arr_aux[i - p] = arr[i];
       num_changes_merge++;
   }

   for(j = q + 1; j <= r; j++){
       arr_aux[r + q + 1 - j - p] = arr[j];
       num_changes_merge++;
   }

    i = p;
    j = r;
    for (k = p; k <= r; k++){
        num_comparisions_merge++;
        if (arr_aux[i - p] <= arr_aux[j - p]) {
            num_changes_merge++;
            arr[k] = arr_aux[i - p];
            i = i + 1;
        }
        else {
            num_changes_merge++;
            arr[k] = arr_aux[j - p];
            j = j - 1;
        
        }
    }
        
}

void mergeSort(int arr[], int l, int r) {
   int m;

   num_comparisions_merge++;
   if(l < r) {
      int m = l+(r-l)/2;

      mergeSort(arr, l, m);
      mergeSort(arr, m+1, r);
      merge(arr, l, m, r);
   }
}

void mergeSortCaller(int arr[], int n){
    mergeSort(arr, 0, n);
    cout << "comparisions made: " << num_comparisions_merge << " / changes made: " << num_changes_merge << endl;
}
