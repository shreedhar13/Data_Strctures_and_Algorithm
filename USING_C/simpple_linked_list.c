#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
   struct node *head;
   head=malloc(sizeof(struct node));//not neccessory to mention return type of malloc(),,bcz malloc will automatically recognize the return type by seeing struct node in its argument type
   head->data=5;
   head->next=NULL;
   printf("%d %d",head->data,head->next);
}