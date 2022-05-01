/*
Mostre como implementar uma fila usando duas pilhas. Analise o tempo de execução das operações sobre as filas.
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