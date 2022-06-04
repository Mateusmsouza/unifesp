// C++ Implementation of the Quick Sort Algorithm.
#include <iostream>
using namespace std;

int partition(int arr[], int p, int r)
{
    int temp;
    int i;
    temp = arr[r];
    i = p-1;

    for(int j = p; j <= r-1; j++){
        if(arr[j] <= temp){
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[r]);
    return i+1;
}

void quickSort(int arr[], int p, int r)
{
    if(p < r){
        int q = partition(arr, p, r);
	    quickSort(arr, p, q - 1);
	    quickSort(arr, q + 1, r);
    }
}

void print(int arr[], int n){
    for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
    cout << endl;
}

int main()
{
	int arr[] = { 6,4,3,2,1 };
	int n = 5;

	quickSort(arr, 0, n - 1);
	print(arr, n);
	return 0;
}
