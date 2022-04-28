/*
Considere uma pilha P vazia e uma fila F não vazia. Utilizando apenas os testes de fila
e pilha vazias, as operações TFila Enfileira, TFila Desenfileira, TPilha Empilha,
TPilha Desempilha, e uma variável aux do tipo TItem, escreva um procedimento que
inverte a ordem dos elementos da fila.
*/
#include <stack>
#include <bits/stdc++.h>
using namespace std;

void PrintStack(stack<int> Stack)
{
    while (!Stack.empty()) {
        cout << Stack.top() << " ";
        Stack.pop();
    }
}

void RevertStack(stack<int>& Stack){
    if(!Stack.empty()){
        int aux = Stack.top();
        Stack.pop();
        RevertStack(Stack);
        Stack.push(aux);
    }
}

void PrintQueue(queue<int> Queue)
{
    while (!Queue.empty()) {
        cout << Queue.front() << " ";
        Queue.pop();
    }
}

void RevertQueue(queue<int>& Queue){
    if(!Queue.empty()){
        int aux = Queue.front();
        Queue.pop();
        RevertQueue(Queue);
        Queue.push(aux);
    }
}

int main(){
    // stack revert
    stack<int> Stack;
    Stack.push(1);
    Stack.push(2);
    Stack.push(3);
    Stack.push(4);
    cout << "reverting stack... \n";
    RevertStack(Stack);
    cout << "stack reversed:... \n";
    PrintStack(Stack);

    // queue revert
    queue<int> Queue;
    Queue.push(1);
    Queue.push(2);
    Queue.push(3);
    Queue.push(4);

    cout << "\n\nreverting queue... \n";
    RevertQueue(Queue);
    cout << "queue reversed:... \n";
    PrintQueue(Queue);
    cout << "\n";
    return 1;
}