#include "lists.h"

/**
 * print_dlistint - prints elements of a list
 *@h: head
 *Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t counter = 0;
	
	while (h)
	{
		printf("%d\n",h->n); 
		counter++;
		h = h->next;
	}

return(counter);
}
 
	
