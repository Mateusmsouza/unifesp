#include <bits/stdc++.h>
using namespace std;

void insertionSort(int arr[], int n){
	int i, j, selected;
	for (i = 1; i < n; i++){
		selected = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > selected){
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = selected;
	}
}
