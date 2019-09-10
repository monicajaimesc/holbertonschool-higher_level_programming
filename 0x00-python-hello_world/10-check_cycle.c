#include "lists.h"

int check_cycle(listint_t *list)
{
	int cycle = 0;
	
	if(!list)
	return(0);

	while(list)
	{
		list = list->next;
		cycle++;
		if (cycle > 9)
		return(1);
	}

return(0);
}

