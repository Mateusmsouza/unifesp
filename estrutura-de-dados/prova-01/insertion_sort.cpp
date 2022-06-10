#include <bits/stdc++.h>
using namespace std;

void insertionSort(int arr[], int n){
	int num_comparisions_insertion = 0;
    int num_changes_insertion = 0;

	int i, j, selected;
	for (i = 1; i < n; i++){
		selected = arr[i];
		j = i - 1;
		num_comparisions_insertion++;
		while (j >= 0 && arr[j] > selected){
			num_changes_insertion++;
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		num_changes_insertion++;
		arr[j + 1] = selected;
	}
    cout << "comparisions made: " << num_comparisions_insertion << " / changes made: " << num_changes_insertion << endl;
}
