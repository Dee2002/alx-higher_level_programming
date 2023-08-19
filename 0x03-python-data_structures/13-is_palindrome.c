#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to pointer to the head of the list
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev = NULL;
listint_t *second_half, *mid = NULL;
int palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid = slow;
slow = slow->next;
}

second_half = slow;
prev->next = NULL;
reverse_list(&second_half);
palindrome = compare_lists(*head, second_half);

if (mid != NULL)
{
prev->next = mid;
mid->next = second_half;
}
else
{
prev->next = second_half;
}

return (palindrome);
}

/**
* reverse_list - reverses a linked list
* @head: pointer to pointer to the head of the list
*/
void reverse_list(listint_t **head)
{
listint_t *prev = NULL, *current = *head, *next;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
* compare_lists - compares two linked lists
* @list1: pointer to the head of the first list
* @list2: pointer to the head of the second list
* Return: 1 if the lists are equal, 0 if not
*/
int compare_lists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n != list2->n)
return (0);
list1 = list1->next;
list2 = list2->next;
}

return (list1 == NULL && list2 == NULL);
}
