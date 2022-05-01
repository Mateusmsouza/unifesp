/*Uma palavra é um palíndromo se a sequência de letras que a forma é a mesma seja ela lida da
esquerda para a direita, ou da direita para esquerda. Exemplos: arara, raiar, hanah. Escreva
um programa que leia uma palavra e, usando uma fila ou uma pilha (decida qual é mais
conveniente), decida se ela é um palíndromo.*/
#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

int main(){
    stack<char> Stack;
    string line;
    string reversedLine;
    bool is_palindrom;

    getline(std::cin, line);

    for(char& c : line) {
        Stack.push(c);
    }

    while(!Stack.empty()){
        char c = Stack.top();
        Stack.pop();
        reversedLine = reversedLine + c;
    }

    is_palindrom = reversedLine == line;

    cout << "\né palindrome: \n";
    cout << is_palindrom << "\n";
    return 0;
}