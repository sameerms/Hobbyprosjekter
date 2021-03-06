#include <NumPyArray.h>

int NumPyArray_Float:: checktype () const
{
  if (a->descr->type_num != PyArray_DOUBLE) {
    PyErr_Format(PyExc_ValueError,
		 "a is not of type 'Float'");
    return 0;
  }
  return 1;
}

int NumPyArray_Float:: checkdim (int expected_ndim) const
{
  if (a->nd != expected_ndim) {
    PyErr_Format(PyExc_ValueError,
		 "NumPy array is %d-dimensional; expected %d dimensions", 
		 a->nd, expected_ndim);
    return 0;
  } 
  return 1;
}

int NumPyArray_Float:: checksize (int expected_size1, 
				  int expected_size2, 
				  int expected_size3) const
{
  if (a->dimensions[0] != expected_size1) {
    PyErr_Format(PyExc_ValueError,
		 "NumPy array's 1st index runs from 0 to %d (expected %d)", 
		 a->dimensions[0], expected_size1);
    return 0;
  }
  if (expected_size2 > 0) {
    if (a->dimensions[1] != expected_size1) {
	PyErr_Format(PyExc_ValueError,
		     "NumPy array's 2nd index runs from 0 to %d (expected %d)", 
		     a->dimensions[1], expected_size2);
	return 0;
    }
    if (expected_size3 > 0) {
      if (a->dimensions[2] != expected_size3) {
	PyErr_Format(PyExc_ValueError,
		     "NumPy array's 3rd index runs from 0 to %d (expected %d)", 
		     a->dimensions[2], expected_size3);
	return 0;
      }
    }
  }
  return 1;
}


int NumPyArray_Float:: create (int n) 
{ 
  printf("Creating array(%d)\n", n);
  int dim1[1]; dim1[0] = n; 
  a = (PyArrayObject*) PyArray_FromDims(1, dim1, PyArray_DOUBLE);
  if (a == NULL) { 
    printf("creating NumPyArray in C failed, dim=(%d)\n", n);
    return 0;
  }
  return 1;
}

int NumPyArray_Float:: create (int n1, int n2) 
{ 
  printf("Creating array(%d,%d)\n", n1, n2);
  int dim2[2]; dim2[0] = n1; dim2[1] = n2;
  a = (PyArrayObject*) PyArray_FromDims(2, dim2, PyArray_DOUBLE);
  if (a == NULL) { 
    printf("creating a failed, dims=(%d,%d)\n",n1, n2);
    return 0;
  }
  return 1;
}

int NumPyArray_Float:: create (int n1, int n2, int n3) 
{ 
  int dim3[3]; dim3[0] = n1; dim3[1] = n2; dim3[2] = n3;
  a = (PyArrayObject*) PyArray_FromDims(3, dim3, PyArray_DOUBLE);
  if (a == NULL) { 
    printf("creating a failed, dims=(%d,%d,%d)\n",n1, n2, n3);
    return 0;
  }
  return 1;
}

void dump (std::ostream& o, const NumPyArray_Float& a)
{
  int i,j,k;
  o << "Dump of NumPyArray object:\n";
  if (a.dim() == 1) {
    for (i = 0; i < a.size1(); i++) {
      o << "(" << i << ")=" << a(i) << " ";
      if (i % 6 == 0) { o << '\n'; }
    }
  }
  if (a.dim() == 2) {
    for (i = 0; i < a.size1(); i++) {
      for (j = 0; j < a.size2(); j++) {
	o << "(" << i << "," << j << ")=" << a(i,j) << " ";
	if (i % 5 == 0) { o << '\n'; }
      }
    }
  }
  if (a.dim() == 3) {
    for (i = 0; i < a.size1(); i++) {
      for (j = 0; j < a.size2(); j++) {
	for (k = 0; k < a.size3(); k++) {
	  o << "(" << i << "," << j << "," << k << ")=" << a(i,j,k) << " ";
	  if (i % 4 == 0) { o << '\n'; }
	}
      }
    }
  }
}
