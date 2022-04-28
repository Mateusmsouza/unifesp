/*
Considere uma pilha P vazia e uma fila F não vazia. Utilizando apenas os testes de fila
e pilha vazias, as operações TFila Enfileira, TFila Desenfileira, TPilha Empilha,
TPilha Desempilha, e uma variável aux do tipo TItem, escreva um procedimento que
inverte a ordem dos elementos da fila.
*/
#include <stack>
#include <bits/stdc++.h>
using namespace std;

class QueueWithStacks {
        stack<int> StackA;
        stack<int> StackB;
    public:
        void enqueue(int);
        int dequeue();
};

void QueueWithStacks::enqueue(int n){
    StackA.push(n);
};

int QueueWithStacks::dequeue(){
    if(StackA.empty() && StackB.empty()){
        return -1;
    } else {
        while(!StackA.empty()){
            int aux = StackA.top();
            StackA.pop();
            StackB.push(aux);
        }
    }
    int top = StackB.top();

    while(!StackB.empty()){
        StackA.push(StackB.top());
        StackB.pop();
    }

    return top;
};

int main(){
    QueueWithStacks Queue;

    Queue.enqueue(1);
    Queue.enqueue(2);
    Queue.enqueue(3);
    Queue.enqueue(4);

    cout << Queue.dequeue() << "";
    cout << Queue.dequeue() << "";
    return 1;
}