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