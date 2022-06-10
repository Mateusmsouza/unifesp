#include <iostream>
#include <ctime>
#include "custom_sort.h"

using namespace std;

const string ALGO_ON_TEST = "BubbleSort";
clock_t time_req;

void execute_test(const char* data_path, const char* algo_on_test, const char* test_type, int array_size, void (*sort)(int[], int) ){
	int arr[array_size];
	read_array_from_file(data_path, array_size, arr);
	printf("-----------------------------------------------------------\n");
	cout << algo_on_test << " testing on " << test_type << " with an array of size " << array_size << endl;
	time_req = clock();
	sort(arr, array_size);
	time_req = clock() - time_req;
	cout << "time consumed by " << algo_on_test << " ordering an array " << test_type << " of size " << array_size << " was " << (float)time_req/CLOCKS_PER_SEC << " seconds " << endl;
	printf("-----------------------------------------------------------\n");
}

void suite_test(const char* unsorted_data, const char* sorted_data, const char* reversed_sorted_data, const char* almost_sorted_data, int n){
	// Run Tests on QuickSort
	execute_test(unsorted_data, "Quick Sort", "Unsorted Data", n, quickSortCaller);
	execute_test(sorted_data, "Quick Sort", "Sorted Data", n, quickSortCaller);
	execute_test(reversed_sorted_data, "Quick Sort", "Reversed Sorted Data", n, quickSortCaller);
	execute_test(almost_sorted_data, "Quick Sort", "Almost Sorted Data", n, quickSortCaller);

	// Run Tests on MergeSort
	execute_test(unsorted_data, "Merge Sort", "Unsorted Data", n, mergeSortCaller);
	execute_test(sorted_data, "Merge Sort", "Sorted Data", n, mergeSortCaller);
	execute_test(reversed_sorted_data, "Merge Sort", "Reversed Sorted Data", n, mergeSortCaller);
	execute_test(almost_sorted_data, "Merge Sort", "Almost Sorted Data", n, mergeSortCaller);

	// Run Tests on HeapSort
	execute_test(unsorted_data, "Heap Sort", "Unsorted Data", n, heapSort);
	execute_test(sorted_data, "Heap Sort", "Sorted Data", n, heapSort);
	execute_test(reversed_sorted_data, "Heap Sort", "Reversed Sorted Data", n, heapSort);
	execute_test(almost_sorted_data, "Heap Sort", "Almost Sorted Data", n, heapSort);

	// Run Tests on Insertion Sort
	execute_test(unsorted_data, "Insertion Sort", "Unsorted Data", n, insertionSort);
	execute_test(sorted_data, "Insertion Sort", "Sorted Data", n, insertionSort);
	execute_test(reversed_sorted_data, "Insertion Sort", "Reversed Sorted Data", n, insertionSort);
	execute_test(almost_sorted_data, "Insertion Sort", "Almost Sorted Data", n, insertionSort);

	// Run Tests on Selection Sort
	execute_test(unsorted_data, "Selection Sort", "Unsorted Data", n, selectionSort);
	execute_test(sorted_data, "Selection Sort", "Sorted Data", n, selectionSort);
	execute_test(reversed_sorted_data, "Selection Sort", "Reversed Sorted Data", n, selectionSort);
	execute_test(almost_sorted_data, "Selection Sort", "Almost Sorted Data", n, selectionSort);
	
	// Run Tests on Bubble Sort
	execute_test(unsorted_data, "Bubble Sort", "Unsorted Data", n, bubbleSort);
	execute_test(sorted_data, "Bubble Sort", "Sorted Data", n, bubbleSort);
	execute_test(reversed_sorted_data, "Bubble Sort", "Reversed Sorted Data", n, bubbleSort);
	execute_test(almost_sorted_data, "Bubble Sort", "Almost Sorted Data", n, bubbleSort);

	// Run Tests on Stooge Sort
	execute_test(unsorted_data, "Stooge Sort", "Unsorted Data", n, stoogeSortCaller);
	execute_test(sorted_data, "Stooge Sort", "Sorted Data", n, stoogeSortCaller);
	execute_test(reversed_sorted_data, "Stooge Sort", "Reversed Sorted Data", n, stoogeSortCaller);
	execute_test(almost_sorted_data, "Stooge Sort", "Almost Sorted Data", n, stoogeSortCaller);
}


void test_ten(){
	const char* unsorted_data = "./data/unsorted/data_10.txt";
	const char* sorted_data = "./data/sorted/data_10.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_10.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_10.txt";
	const int n = 10;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

void test_hundred(){
	const char* unsorted_data = "./data/unsorted/data_100.txt";
	const char* sorted_data = "./data/sorted/data_100.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_100.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_100.txt";
	const int n = 100;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

void test_thousand(){
	const char* unsorted_data = "./data/unsorted/data_1000.txt";
	const char* sorted_data = "./data/sorted/data_1000.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_1000.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_1000.txt";
	const int n = 1000;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

void test_ten_thousand(){
	const char* unsorted_data = "./data/unsorted/data_10000.txt";
	const char* sorted_data = "./data/sorted/data_10000.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_10000.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_10000.txt";
	const int n = 10000;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

void test_hundred_thousand(){
	const char* unsorted_data = "./data/unsorted/data_100000.txt";
	const char* sorted_data = "./data/sorted/data_100000.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_100000.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_100000.txt";
	const int n = 100000;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

void test_a_million(){
	const char* unsorted_data = "./data/unsorted/data_100000.txt";
	const char* sorted_data = "./data/sorted/data_100000.txt";
	const char* reversed_sorted_data = "./data/reversed_sorted/data_100000.txt";
	const char* almost_sorted_data = "./data/almost_sorted/data_100000.txt";
	const int n = 1000000;
	suite_test(unsorted_data, sorted_data, reversed_sorted_data, almost_sorted_data, n);
}

int main(){
	cout << fixed;
	test_ten();
	test_hundred();
	test_thousand();
	//test_ten_thousand();
	//test_hundred_thousand();
	//test_a_million();
}