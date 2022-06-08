#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[], int n){
    int i, j;
    for (i = 0 ; i < n-1 ; i++){
        for (j = 1 ; j < n-i ; j++){
            if (arr[j] < arr[j-1]) swap(arr[j], arr[j-1]);
        }
    }
}
