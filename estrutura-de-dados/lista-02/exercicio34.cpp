#include <iostream>
using namespace std;

void oddEvenSort(int arr[], int n){
    bool sorted = false;

    while(!sorted){
        sorted = true;

        // odd looping
        for(int i=1; i<=n-2; i=i+2){
            if(arr[i] > arr[i+1]){
                swap(arr[i], arr[i+1]);
                sorted = false;
            }
        }

        // even looping
        for(int i=0; i<=n-2; i=i+2){
            if(arr[i] > arr[i+1]){
                swap(arr[i], arr[i+1]);
                sorted = false;
            }
        }
    }
}

int main(){
    int arr[] = {4, 3, 6, 2, 1};
    int n = sizeof(arr)/sizeof(arr[0]);

    oddEvenSort(arr, n);
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}