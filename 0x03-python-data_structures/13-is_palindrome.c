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
	int size = 0, i = 0, sum = 1, j = 0;
	int *list, *new_list;
	listint_t *temp;

	temp = *head;
	if (temp == NULL)
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
	for (i = size - 1, j = 0; i >= 0; i--, j++)
		new_list[j] = list[i];
	for (i = 0; i < size; i++)
	{
		if (list[i] != new_list[i])
		{
			sum = 0;
			break;
		}
	}
	free(list);
	free(new_list);
	return (sum);
}
