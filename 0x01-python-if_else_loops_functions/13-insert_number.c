#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert node in a sorted list
 * @head: address of head
 * @number: value to store in new node
 *
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (temp == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	if (temp->next == NULL)
	{
		if (temp->n < number)
		{
			temp->next = new;
			new->next = NULL;
		}
		else
		{
			*head = new;
			new->next = NULL;
		}
	}
	while (temp)
	{
		if (temp->n < number && (temp->next)->n > number)
		{
			new->next = temp->next;
			temp->next = new;
		}
		temp = temp->next;
	}
	return (new);
}
