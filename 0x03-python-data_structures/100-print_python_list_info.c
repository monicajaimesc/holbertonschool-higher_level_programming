#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 *@p: python object
 *Result: nothin, is a void
 */
 
 void print_python_list_info(PyObject *p)
 {
     int i;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    /* PyListObject subtype of PyObject represents a Python list object */
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
 }
