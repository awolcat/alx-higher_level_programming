#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - look for cycles in singly linked list
 * @list: pointer to head of the list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	int a = 0;

	temp = list;
	while (temp != NULL)
	{
		if (temp->next == temp || temp->next == list)
		{
			a = 1;
			break;
		}
		temp = temp->next;
	}
	return (a);
}
