#!/bin/sh
n=1100

echo "Pure Python:"
python $scripting/src/py/intro/Grid2D.py timing $n
echo

cd F77
echo "F77 stand-alone program:"
perl -pi.old~ -e "s/^\s+parameter \(nmax=.*\)/      parameter (nmax=$n)/" gridloop.f
egrep "^\s+parameter \(nmax" gridloop.f
./make_F77_app.sh
./clean.sh

echo "F77 extension module:"
./make_module_1.sh > /dev/null
python ../Grid2Deff.py timing2 $n
./clean.sh

cd ../C/plain
echo "C extension module; a single handwritten function:"
./make_module_1.sh
python ../../Grid2Deff.py timing2 $n
./clean.sh

cd ../clibcall
echo "C extension module; separate function and handwritten wrapper:"
./make_module_1.sh
python ../../Grid2Deff.py timing2 $n
./clean.sh

cd ../../C++/plain
echo "C++ extension module; handwritten wrapper + class:"
./make_module_1.sh
python ../../Grid2Deff.py timing2 $n
./clean.sh

cd ../scxx
echo "C++ extension module; handwritten wrapper using SCXX:"
./make_module_1.sh
python ../../Grid2Deff.py timing2 $n
./clean.sh

cd ../convertptr
echo "C++ extension module; conversion class wrapped with SWIG:"
./make_module_1.sh
python Grid2Deff2.py timing2 $n
./clean.sh

echo "C++ standalone program (with MyArray and gridloop1):"
./make_Cpp_app.sh $n
./clean.sh


