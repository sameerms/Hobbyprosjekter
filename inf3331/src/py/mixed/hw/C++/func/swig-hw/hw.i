/* file: hw.i */
%module hw
%{
/* include C++ header files necessary to compile the interface */
/* not required here, but typically
#include "hw.h"
*/
%}

%include "typemaps.i"
%apply double *OUTPUT { double* s }
%apply double *OUTPUT { double& s }
%include "hw.h"

