#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts no to sorted list
 * @head: pointer to head node
 * @number: data of the new node
 *
 * Return: address of new node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head, *prev = *head;
	int i, count = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n == number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->n < new->n)
	{
		current = current->next;
		count++;
	}

	for (i = 0; i < count - 1; i++)
		prev = prev->next;

	new->next = current;
	prev->next = new;

	return (new);
}
