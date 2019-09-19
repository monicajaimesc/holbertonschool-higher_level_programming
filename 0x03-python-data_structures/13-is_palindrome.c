#include "lists.h"

/**
 * is_palindrome - checking if a singly list is palindrome
 * @head: header double pointer
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp; /*pointing to the list*/
	int buffer[1000];
	int counter = 0;
	int j = 0;
	int i = 0;

		temp = *head;
		if (head == NULL)
			return (1);

		if (*head == NULL)
			return (1);

		if (temp->next == NULL)
			return (1);

		while (temp)
		{
			buffer[counter] = temp->n;
			temp = temp->next;
			i++;
			counter++;

		}

		counter = counter - 1;

		while (j <= counter)
		{

			if (buffer[i] != buffer[j])
			counter--;
			j++;
		}
		return (1);
}
