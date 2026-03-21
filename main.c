#include <stdio.h>
#include <stdlib.h>

#define  n 100

int queue[n];
int front = -1, rear = -1;

void display()
{
    if (front == -1 && rear == -1)
    {
        printf("Queue is empty\n");
        return;
    }

    int i = front;
    printf("Queue elements: ");
    while (i != rear)
    {
        printf("%d ", queue[i]);
        i = (i + 1) % n;
    }
    printf("%d\n", queue[rear]); // print the last element
}
