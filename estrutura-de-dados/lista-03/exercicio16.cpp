/*
Forneça um procedimento não recursivo de tempo Θ(n) que inverta uma lista simplesmente
encadeada de n elementos. Qualquer consumo de memória além em do espaço de armazenamento necessário para a própria lista deve ter tamanho O(1).
*/
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Node{
    public:
        int value;
        Node* next;
};

Node* revert(Node* LinkedList, Node* NewLinkedList){
    if(LinkedList == NULL){
        return NewLinkedList;
    }

    Node* currentNode = new Node();
    currentNode->value = LinkedList->value; 
    Node* nextNode = revert(LinkedList->next, NewLinkedList);
    nextNode->next = currentNode;

    return currentNode;
}


int main(){
    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    // allocate 3 nodes in the heap
    one = new Node();
    two = new Node();
    three = new Node();

    // Assign value values
    one->value = 1;
    two->value = 2;
    three->value = 3;
    one->next = two;
    two->next = three;
    three->next = NULL;

    head = one;
    Node* newHead = new Node();

    revert(head, newHead);
    Node* reversedList = newHead->next;
    while (reversedList != NULL) {
        cout << reversedList->value;
        cout << "\n";
        reversedList = reversedList->next;
    }

    return 1;
}