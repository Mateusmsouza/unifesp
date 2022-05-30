/*
Desenvolva um algoritmo usando um heap de k elementos para encontrar os maiores k n ́umeros
num grande vetor n ̃ao ordenado de n n ́umeros, em que n >> k.
*/
#include <iostream>

using namespace std;

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

    if(largest != i){
        swap(arr[i], arr[largest]);
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

        heapify(arr, i, 0);
    }
}

void print(int arr[], int n){
    cout << "[ ";
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << "]";
    cout << "\n";
}

int main(){

    int arr[] = {4,8,1,2,9,4,7,4,2};
    int n  = sizeof(arr)/sizeof(arr[0]);

    /*in order to find biggest k numbers in arr, k must be k << n*/
    int k = n - 4;

    heapSort(arr, k);
    print(arr, k);
}