#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - check if a list is a palindrome or not
 * @head: pointer to head of list
 *
 * Return: 0 if not palindrome else return 1
 */
int is_palindrome(listint_t **head)
{
	int size = 0, i = 0, sum = 0;
	int *list, *new_list;
	listint_t *temp;

	temp = *head;
	if (temp->next == NULL || temp == NULL)
		return (1);
	for (size = 0; temp; size++)
		temp = temp->next;
	temp = *head;
	list = malloc(sizeof(int) * size);
	for (i = 0; temp; i++)
	{
		list[i] = temp->n;
		temp = temp->next;
	}
	new_list = malloc(sizeof(int) * size);
	for (i = 0; i < size; i++)
		new_list[i] = list[i];
	for (i = 0; i < size; i++)
	{
		if (list[i] < 0)
			list[i] = -list[i];
		if (new_list[i] < 0)
			new_list[i] = -new_list[i];
		sum += (new_list[i] - list[i]);
	}
	if (sum == 0)
		return (1);
	return (0);
}
