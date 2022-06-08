#include <iostream>
#include "custom_sort.h"

using namespace std;

void print(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

void test_ten(){
	//printf("Starting benhmark for an array of size 10\n");

	const char* data = "./data/unsorted/data_10.txt";
	const int n = 10;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

void test_hundred(){
	//printf("Starting benhmark for an array of size 100\n");

	const char* data = "./data/unsorted/data_100.txt";
	const int n = 100;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

void test_thousand(){
	//printf("Starting benhmark for an array of size 1000\n");

	const char* data = "./data/unsorted/data_1000.txt";
	const int n = 1000;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

void test_ten_thousand(){
	//printf("Starting benhmark for an array of size 10000\n");

	const char* data = "./data/unsorted/data_10000.txt";
	const int n = 10000;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

void test_hundred_thousand(){
	//printf("Starting benhmark for an array of size 100000\n");

	const char* data = "./data/unsorted/data_100000.txt";
	const int n = 100000;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

void test_a_million(){
	//printf("Starting benhmark for an array of size 1000000\n");

	const char* data = "./data/unsorted/data_1000000.txt";
	const int n = 1000000;
	int arr[n];
	read_array_from_file(data, n, arr);

    //bubbleSort(arr10, n);
	//mergeSort(arr10, 0, n);
	quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	print(arr, n);
}

int main(){
	//test_ten();
	//test_hundred();
	//test_thousand();
	//test_ten_thousand();
	//test_hundred_thousand();
	test_a_million();
}