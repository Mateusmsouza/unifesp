#include <cmath>
#include <iostream>

using namespace std;

int num_comparisions_stooge = 0;
int num_changes_stooge = 0;

void stoogeSort(int arr[], int left, int right){
    num_comparisions_stooge=num_comparisions_stooge+2;
    if (left >= right) return;
    if (arr[left] > arr[right]){
        num_changes_stooge++;
        swap(arr[left], arr[right]);
    }
    if ((right - left + 1) > 2){
        int t = floor((right - left + 1)/3);
        stoogeSort(arr, left, right - t);
        stoogeSort(arr, left + t, right);
        stoogeSort(arr, left, right - t);
    }
}

void stoogeSortCaller(int arr[], int n){
    stoogeSort(arr, 0, n-1);
    cout << "comparisions made: " << num_comparisions_stooge << " / changes made: " << num_changes_stooge << endl;
}