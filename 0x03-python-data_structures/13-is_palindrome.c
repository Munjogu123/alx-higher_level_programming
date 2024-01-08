#include "lists.h"

/**
 * reverse_listint - reverses a list
 * @head: pointer to list
 *
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	prev = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	(*head) = prev;
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

	start = *head;
	end = *head;
	mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		end = end->next->next;
		if (end == NULL)
		{
			mid = start->next;
			break;
		}
		if (end->next == NULL)
		{
			mid = start->next->next;
			break;
		}
		start = start->next;
	}
	reverse_listint(&mid);
	while (*head && mid)
	{
		if ((*head)->n == mid->n)
		{
			*head = (*head)->next;
			mid = mid->next;
		} else
		{
			return (0);
		}
	}
	if (!mid)
		return (1);
	return (0);
}
