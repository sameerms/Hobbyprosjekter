#include <Python.h>
#include <Numeric/arrayobject.h>
#include <convert.h>

Convert_MyArray:: Convert_MyArray()
{
  import_array();
}

PyObject* Convert_MyArray:: my2py(MyArray<double>& a)
{
  //a.dump(std::cout);
  PyArrayObject* array =  (PyArrayObject*) \
          PyArray_FromDimsAndData(a.ndim, a.size, PyArray_DOUBLE,
				  (char*) a.A); 
  if (array == NULL) {
    return NULL; /* PyArray_FromDimsAndData raised an exception */ 
  }
  return PyArray_Return(array);
}

PyObject* Convert_MyArray:: my2py_copy(MyArray<double>& a)
{
  //a.dump(std::cout);
  PyArrayObject* array =  (PyArrayObject*) \
          PyArray_FromDims(a.ndim, a.size, PyArray_DOUBLE); 
  if (array == NULL) {
    return NULL; /* PyArray_FromDims raised an exception */ 
  }
  double* ad = (double*) array->data;
  for (int i = 0; i < a.length; i++) {
    ad[i] = a.A[i];
  }
  return PyArray_Return(array);
}

MyArray<double>* Convert_MyArray:: py2my(PyObject* a_)
{
  PyArrayObject* a = (PyArrayObject*) 
    PyArray_ContiguousFromObject(a_, PyArray_DOUBLE, 0, 0);
  if (a == NULL) { return NULL; }
  /*
  PyArrayObject* a = (PyArrayObject*) a_;
  if (a->descr->type_num != PyArray_DOUBLE) {
    PyErr_SetString(PyExc_TypeError, "Not an array of double");
    return NULL;
  }
  */
  // borrow the data, but wrap it in MyArray:
  MyArray<double>* ma = new MyArray<double> \
      ((double*) a->data, a->nd, a->dimensions);
  return ma;
}

MyArray<double>* Convert_MyArray:: py2my_copy(PyObject* a_)
{
  PyArrayObject* a = (PyArrayObject*) 
    PyArray_ContiguousFromObject(a_, PyArray_DOUBLE, 0, 0);
  if (a == NULL) { return NULL; }
  /*
  PyArrayObject* a = (PyArrayObject*) a_;
  if (a->descr->type_num != PyArray_DOUBLE) {
    PyErr_SetString(PyExc_TypeError, "Not an array of double");
    return NULL;
  }
  */
  MyArray<double>* ma = new MyArray<double>();
  if (a->nd == 1) {
    ma->redim(a->dimensions[0]);
  } else if (a->nd == 2) {
    ma->redim(a->dimensions[0], a->dimensions[1]);
  } else if (a->nd == 3) {
    ma->redim(a->dimensions[0], a->dimensions[1], a->dimensions[2]);
  }
  // copy data:
  double* ad = (double*) a->data;
  double* mad = ma->A;
  for (int i = 0; i < ma->length; i++) {
    mad[i] = ad[i];
  }
  return ma;
}

double Convert_MyArray:: _pycall (double x, double y)
{
  PyObject* arglist = Py_BuildValue("(dd)", x, y);
  PyObject* result =  PyEval_CallObject(\
                      Convert_MyArray::_pyfunc_ptr, arglist);
  Py_DECREF(arglist);
  if (result == NULL) { /* cannot return NULL... */
    printf("Error in callback..."); exit(1);
  }
  double C_result = PyFloat_AS_DOUBLE(result);
  Py_DECREF(result); 
  return C_result;
}

PyObject* Convert_MyArray::_pyfunc_ptr = NULL;
  
Fxy Convert_MyArray:: set_pyfunc (PyObject* f)
{
  _pyfunc_ptr = f;
  Py_INCREF(_pyfunc_ptr);
  return _pycall;
}

void Convert_MyArray:: dump(MyArray<double>& a)
{
  a.print(std::cout);
}

