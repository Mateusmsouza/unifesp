#include <bits/stdc++.h>
using namespace std;

void selectionSort(int arr[], int n){
	int num_comparisions_select = 0;
    int num_changes_select = 0;

	int i, j, min_element;
	for (i = 0; i < n-1; i++)
	{
		min_element = i;
		for (j = i+1; j < n; j++){
			num_comparisions_select ++;
			if (arr[j] < arr[min_element]){
				 min_element = j;
			}
		}
		
		num_changes_select++;
		swap(arr[min_element], arr[i]);
	}
    cout << "comparisions made: " << num_comparisions_select << " / changes made: " << num_changes_select << endl;
}
