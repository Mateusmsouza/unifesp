#include <iostream>

using namespace std;

int num_comparisions_heap = 0;
int num_changes_heap = 0;

/*
arr: heap as an array
n: heap size (array size)
i: current root heap index
*/
void heapify(int arr[], int n, int i){
    int largest = i;
    int left = 2*i+1;
    int right = 2*i+2;

    if(left < n && arr[left] > arr[largest]){
        largest = left;
    }

    if(right < n && arr[right] > arr[largest]){
        largest = right;
    }
    num_comparisions_heap = num_comparisions_heap + 2;
    if(largest != i){
        swap(arr[i], arr[largest]);
        num_changes_heap++;
        heapify(arr, n, largest);
    }
}

void buildHeap(int arr[], int n){
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}

void heapSort(int arr[], int n){
    buildHeap(arr, n);

    for (int i=n-1; i>=0; i--){
        swap(arr[0], arr[i]);
        num_changes_heap++;
        heapify(arr, i, 0);
    }

    cout << "comparisions made: " << num_comparisions_heap << " / changes made: " << num_changes_heap << endl;
}
