#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;

void read_array_from_file(const char* file_path, const int array_size, int* arr){
    ifstream file(file_path);

    if(file.is_open()){
        for(int j = 0; j < array_size; j++) file >> arr[j];
    }
};