#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[], int n){
    int num_comparisions_bubble = 0;
    int num_changes_bubble = 0;
    int i, j;
    for (i = 0 ; i < n-1 ; i++){
        num_comparisions_bubble++;
        for (j = 1 ; j < n-i ; j++){
            if (arr[j] < arr[j-1]) {
                swap(arr[j], arr[j-1]);
                num_changes_bubble++;
            }
        }
    }

    cout << "comparisions made: " << num_comparisions_bubble << " / changes made: " << num_changes_bubble << endl;
}
