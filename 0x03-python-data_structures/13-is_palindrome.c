#include "lists.h"
/**
 * list_len - Return the length of the linked list
 * @h: Linked list head
 * Return: Length of the linked list, 0 otherwise
 */
int list_len(listint_t *h)
{
	int idx;

	if (h == NULL)
		return (-1);

	for (idx = 0; h != NULL; ((h = h->next), idx++))
		;

	return (idx);
}

/**
 * is_palindrome - A function that checks if the list is a palindrome
 * @head: Linked list head
 * Return: 1 if the list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int len = list_len(*head);
	int *arr = malloc(1 * len), idx, idy;

	if (!head || ptr == NULL || arr == NULL)
	{
		free(arr);
		return (-1);
	}
	
	for (idx = 0; ptr != NULL; ((ptr = ptr->next), idx++))
		arr[idx] = ptr->n;

	for (idy = 0; arr[idy] && idy < idx; idy++)
	{
		if (arr[idy] == arr[(idx - 1) - idy])
			continue;
		else
			return (0);
	}
	return (1);
}
