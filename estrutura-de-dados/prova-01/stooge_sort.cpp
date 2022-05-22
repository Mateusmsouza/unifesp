#include <cmath>
#include <iostream>

using namespace std;

void stoogeSort(int arr[], int left, int right){
    if (left >= right) return;
    if (arr[left] > arr[right]) swap(arr[left], arr[right]);
    if ((right - left + 1) > 2){
        int t = floor((right - left + 1)/3);
        stoogeSort(arr, left, right - t);
        stoogeSort(arr, left + t, right);
        stoogeSort(arr, left, right - t);
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

    stoogeSort(arr, 0, n-1);
    print(arr, n);
}