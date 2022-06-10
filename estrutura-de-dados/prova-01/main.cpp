#include <iostream>
#include <ctime>
#include "custom_sort.h"

using namespace std;

const string ALGO_ON_TEST = "BubbleSort";
clock_t time_req;

void print(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

void test_ten(){
	const char* data = "./data/unsorted/data_10.txt";
	const int n = 10;
	int arrUnsortedData[n];
	read_array_from_file(data, n, arr);
	time_req = clock();

    bubbleSort(arr, n);
	//mergeSort(arr, 0, n);
	//quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	time_req = clock() - time_req;

	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 10 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

void test_hundred(){
	const char* data = "./data/unsorted/data_100.txt";
	const int n = 100;
	int arr[n];
	read_array_from_file(data, n, arr);
	time_req = clock();

    bubbleSort(arr, n);
	//mergeSort(arr, 0, n);
	//quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	time_req = clock() - time_req;
	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 100 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

void test_thousand(){
	const char* data = "./data/unsorted/data_1000.txt";
	const int n = 1000;
	int arr[n];
	read_array_from_file(data, n, arr);
	time_req = clock();

    bubbleSort(arr, n);
	//mergeSort(arr, 0, n);
	//quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	time_req = clock() - time_req;
	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 1000 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

void test_ten_thousand(){
	const char* data = "./data/unsorted/data_10000.txt";
	const int n = 10000;
	int arr[n];
	read_array_from_file(data, n, arr);
	time_req = clock();
    bubbleSort(arr, n);
	//mergeSort(arr, 0, n);
	//quickSort(arr, 0, n - 1);
	//stoogeSort(arr10, 0, n-1);
	time_req = clock() - time_req;
	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 10000 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

void test_hundred_thousand(){
	const char* data = "./data/unsorted/data_100000.txt";
	const int n = 100000;
	int arr[n];
	read_array_from_file(data, n, arr);
	time_req = clock();
    bubbleSort(arr, n);
	mergeSort(arr, 0, n);
	quickSort(arr, 0, n - 1);
	stoogeSort(arr10, 0, n-1);
	time_req = clock() - time_req;
	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 100000 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

void test_a_million(){
	const char* data = "./data/unsorted/data_1000000.txt";
	const int n = 1000000;
	int arr[n];
	read_array_from_file(data, n, arr);
	time_req = clock();
    bubbleSort(arr, n);
	mergeSort(arr, 0, n);
	stoogeSort(arr10, 0, n-1);
	quickSort(arr, 0, n - 1);
	time_req = clock() - time_req;
	cout << "time consumed by " << ALGO_ON_TEST << " ordering an array of size 1000000 was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
}

int main(){
	test_ten();
	test_hundred();
	test_thousand();
	test_ten_thousand();
	test_hundred_thousand();
	test_a_million();
}