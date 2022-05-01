/*
Mostre como implementar uma pilha usando duas filas. Analise o tempo de execução das
operações sobre pilhas.
*/
#include <bits/stdc++.h>
using namespace std;

class StackWithQueue {
        queue<int> QueueA;
        queue<int> QueueB;
        char QueueInUse =  'A';
    public:
        void push(int);
        int pop();
};

void StackWithQueue::push(int n){
    if(QueueInUse == 'A') {
        QueueA.push(n);
    } else {
        QueueB.push(n);
    }
};

int StackWithQueue::pop(){
    int temp = -1;

    if (QueueInUse == 'A') {
        while(QueueA.size() > 1){
            QueueB.push(QueueA.front());
            QueueA.pop();
        }
        temp = QueueA.front();
        QueueA.pop();
        QueueInUse = 'B';
    } else {
        while(QueueB.size() > 1){
            temp = QueueB.front();
            QueueA.push(temp);
            QueueB.pop();
        }
        temp = QueueB.front();
        QueueB.pop();
        QueueInUse = 'A';
    }

    return temp;
};

int main(){
    StackWithQueue Stack;

    Stack.push(1);
    Stack.push(2);
    Stack.push(3);
    Stack.push(4);

    cout << Stack.pop() << "";
    cout << Stack.pop() << "";
    return 1;
}