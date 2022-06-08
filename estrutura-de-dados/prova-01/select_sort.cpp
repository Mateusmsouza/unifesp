#include <bits/stdc++.h>
using namespace std;

void selectionSort(int arr[], int n){
	int i, j, min_element;
	for (i = 0; i < n-1; i++)
	{
		min_element = i;
		for (j = i+1; j < n; j++) if (arr[j] < arr[min_element]) min_element = j;
		swap(arr[min_element], arr[i]);
	}
}
