// C++ Implementation of the Quick Sort Algorithm.
#include <iostream>
using namespace std;

int num_comparisions_quick = 0;
int num_changes_quick = 0;

int partition(int arr[], int p, int r)
{
    int temp;
    int i;
    temp = arr[r];
    i = p-1;

    for(int j = p; j <= r-1; j++){
        num_comparisions_quick++;
        if(arr[j] <= temp){
            i++;
            swap(arr[i], arr[j]);
            num_changes_quick++;
        }
    }
    num_changes_quick++;
    swap(arr[i+1], arr[r]);
    return i+1;
}

void quickSort(int arr[], int p, int r){
    num_comparisions_quick++;
    if(p < r){
        int q = partition(arr, p, r);
	    quickSort(arr, p, q - 1);
	    quickSort(arr, q + 1, r);
    }
}


void quickSortCaller(int arr[], int n){
    quickSort(arr,0,n-1);
    cout << "comparisions made: " << num_comparisions_quick << " / changes made: " << num_changes_quick << endl;
}