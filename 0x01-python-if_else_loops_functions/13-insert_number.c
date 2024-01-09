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

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	new->next = current;
	prev->next = new;

	return (new);
}
