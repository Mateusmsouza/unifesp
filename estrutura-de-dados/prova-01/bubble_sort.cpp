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


void print(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6 };
	int n = sizeof(arr) / sizeof(arr[0]);

	bubbleSort(arr, n);
	print(arr, n);
}
