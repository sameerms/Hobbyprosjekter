


 setmatrix1_py (10 calls): elapsed=130.725, CPU=130.44
 setmatrix1_f_index1 (10 calls): elapsed=101.996, CPU=101.95
 setmatrix1_f_index3 (10 calls): elapsed=50.4362, CPU=50.41
 setmatrix1_f_index4 (10 calls): elapsed=55.3369, CPU=55.29
 setmatrix1_f_loop1 (100 calls): elapsed=3.9786, CPU=3.98



Table: a[i,j] = i*j-2
(one mult+sub per iteration)

                                     C++ loop over C++ array   0.040
                                        Indexing: Matrix_set   5.041
                             Indexing: matrix_cpp.Matrix_set   5.529
                                             Indexing: m.set  10.195
                                 Python loop and NumPy array  13.044



 setmatrix2_py (10 calls): elapsed=227.155, CPU=226.96
 setmatrix2_f_index1 (10 calls): elapsed=187.341, CPU=187.21
 setmatrix2_f_index3 (10 calls): elapsed=123.698, CPU=123.65
 setmatrix2_f_index4 (10 calls): elapsed=131.298, CPU=131.11
 setmatrix2_f_loop1 (100 calls): elapsed=74.5743, CPU=74.54



Table: a[i,j] = i*j-2
(one mult+sub per iteration)

                                     C++ loop over C++ array   0.745
                                        Indexing: Matrix_set  12.365
                             Indexing: matrix_cpp.Matrix_set  13.111
                                             Indexing: m.set  18.721
                                 Python loop and NumPy array  22.696



