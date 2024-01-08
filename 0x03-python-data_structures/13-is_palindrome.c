#include "lists.h"

/**
 * reverse_listint - reverses a list
 * @head: pointer to list
 *
 * Return: pointer to the first node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	prev = NULL;

	if (*head == NULL)
		return (NULL);

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	(*head) = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to head node
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *end, *mid, *start;

	if (*head == NULL)
		return (1);

	while (1)
	{
		end = (*head)->next->next;
		if (end->next == NULL)
		{
			mid = start->next->next;
			break;
		}
		if (end == NULL)
		{
			mid = start->next;
			break;
		}
		start = (*head)->next;
	}
	start->next = NULL;

	reverse_listint(&mid);

	while (*head && mid)
	{
		if ((*head)->n == mid->n)
			return (1);
		*head = (*head)->next;
		mid = mid->next;
	}
	return (0);
}
