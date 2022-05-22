#include <bits/stdc++.h>
using namespace std;

void selectionSort(int arr[], int n)
{
	int i, j, min_element;
	for (i = 0; i < n-1; i++)
	{
		min_element = i;
		for (j = i+1; j < n; j++) if (arr[j] < arr[min_element]) min_element = j;
		swap(arr[min_element], arr[i]);
	}
}

void print(int arr[], int size)
{
	int i;
	for (i=0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arr[] = {64, 25, 12, 22, 11};
	int n = sizeof(arr)/sizeof(arr[0]);
	selectionSort(arr, n);
	print(arr, n);
}