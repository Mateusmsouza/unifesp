/*
Mostre como ordenar n inteiros no intervalo de 1 a n² − 1 em tempo O(n).
*/

#include <iostream>

using namespace std;

void countSort(int arr[], int n, int exp){
    int output[n], count[n], i;

    for(i=0; i<n; i++) count[i] = 0;
    for(i=0; i<n; i++) count[(arr[i]/exp) % n]++;
    for (i = 1; i < n; i++) count[i] += count[i - 1];
    for (i = n - 1; i >= 0; i--)
    {
        output[count[ (arr[i]/exp)%n] - 1] = arr[i];
        count[(arr[i]/exp)%n]--;
    }
    for (i = 0; i < n; i++) arr[i] = output[i];
}

void sort(int arr[], int n){
    countSort(arr, n, 1);
    countSort(arr, n, n);
}

int main()
{
    int arr[] = {2, 5, 3, 1, 6, 4, 90, 87};
    int n = sizeof(arr)/sizeof(arr[0]);
    sort(arr, n);
    for (int j=0; j < n; j++){
        cout << arr[j] << " ";
    }
    cout << "\n";
    return 0;
}