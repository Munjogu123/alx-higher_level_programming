#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a list has a cycle
 * @list: pointer to list
 *
 * Return: 1 if there is a cycle otherwise 0
*/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = list->next;

	while (fast && fast->next)
	{
		if (slow == fast || fast->next == slow->next)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
