./tests.verify: test performed on 2004.08.17 


#### Test: ./tests.verify running simviz1c.py --m 10 --func siny --screenplot 0
CPU time of simviz1c.py: 0.2 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running simviz1cp.py --m 10 --func siny --screenplot 0
tstop= 40
CPU time of simviz1cp.py: 0.4 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running simviz1cp_unit.py -m "10 kg" -func siny --screenplot 0
CPU time of simviz1cp_unit.py: 0.4 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running tmp.sh 
Content-type: text/html


<HTML><BODY BGCOLOR="white">
<IMG SRC="../../../misc/figs/simviz.xfig.gif" ALIGN="right"><P>
<FORM ACTION="wrapper.sh.cgi?s=simviz1cpCGI.py.cgi" METHOD="POST">
<TABLE>
<TR>
<TD>m</TD><TD><INPUT TYPE="text" NAME="m" SIZE=15 VALUE="1.0"></TD><TD>(mass)</TD>
</TR>
<TR>
<TD>b</TD><TD><INPUT TYPE="text" NAME="b" SIZE=15 VALUE="0.7"></TD><TD>(damping)</TD>
</TR>
<TR>
<TD>c</TD><TD><INPUT TYPE="text" NAME="c" SIZE=15 VALUE="5.0"></TD><TD>(stiffness)</TD>
</TR>
<TR>
<TD>func</TD><TD><SELECT NAME="func" SIZE=1 VALUE="y">
<OPTION VALUE="y">y </OPTION>
<OPTION VALUE="y3">y3 </OPTION>
<OPTION VALUE="siny">siny </OPTION>
</SELECT><BR>
</TD><TD>(spring model function)</TD>
</TR>
<TR>
<TD>A</TD><TD><INPUT TYPE="text" NAME="A" SIZE=15 VALUE="5.0"></TD><TD>(forced amplitude)</TD>
</TR>
<TR>
<TD>w</TD><TD><INPUT TYPE="text" NAME="w" SIZE=15 VALUE="6.28318530718"></TD><TD>(forced frequency)</TD>
</TR>
<TR>
<TD>y0</TD><TD><INPUT TYPE="text" NAME="y0" SIZE=15 VALUE="0.2"></TD><TD>(initial displacement)</TD>
</TR>
<TR>
<TD>tstop</TD><TD><INPUT TYPE="text" NAME="tstop" SIZE=15 VALUE="30.0"></TD><TD>(stop time)</TD>
</TR>
<TR>
<TD>dt</TD><TD><INPUT TYPE="text" NAME="dt" SIZE=15 VALUE="0.05"></TD><TD>(time step)</TD>
</TR>
<TR>
<TD>case</TD><TD><INPUT TYPE="text" NAME="case" SIZE=15 VALUE="tmp1"></TD><TD>(case name)</TD>
</TR>
<TR>
<TD>screenplot</TD><TD><INPUT TYPE="checkbox" NAME="screenplot" VALUE="1">&nbsp; <BR>
</TD><TD>(plot on the screen?)</TD>
</TR>

</TABLE><BR>
<INPUT TYPE="submit" VALUE="simulate and visualize" NAME="sim">
</FORM>


</BODY></HTML>

Content-type: text/html


<HTML><BODY BGCOLOR="white">
<IMG SRC="../../../misc/figs/simviz.xfig.gif" ALIGN="right"><P>
<FORM ACTION="wrapper.sh.cgi?s=simviz1cpCGI.py.cgi" METHOD="POST">
<TABLE>
<TR>
<TD>m</TD><TD><INPUT TYPE="text" NAME="m" SIZE=15 VALUE="1.0"></TD><TD>(mass)</TD>
</TR>
<TR>
<TD>b</TD><TD><INPUT TYPE="text" NAME="b" SIZE=15 VALUE="0.7"></TD><TD>(damping)</TD>
</TR>
<TR>
<TD>c</TD><TD><INPUT TYPE="text" NAME="c" SIZE=15 VALUE="5.0"></TD><TD>(stiffness)</TD>
</TR>
<TR>
<TD>func</TD><TD><SELECT NAME="func" SIZE=1 VALUE="y">
<OPTION VALUE="y">y </OPTION>
<OPTION VALUE="y3">y3 </OPTION>
<OPTION VALUE="siny">siny </OPTION>
</SELECT><BR>
</TD><TD>(spring model function)</TD>
</TR>
<TR>
<TD>A</TD><TD><INPUT TYPE="text" NAME="A" SIZE=15 VALUE="5.0"></TD><TD>(forced amplitude)</TD>
</TR>
<TR>
<TD>w</TD><TD><INPUT TYPE="text" NAME="w" SIZE=15 VALUE="6.28318530718"></TD><TD>(forced frequency)</TD>
</TR>
<TR>
<TD>y0</TD><TD><INPUT TYPE="text" NAME="y0" SIZE=15 VALUE="0.2"></TD><TD>(initial displacement)</TD>
</TR>
<TR>
<TD>tstop</TD><TD><INPUT TYPE="text" NAME="tstop" SIZE=15 VALUE="30.0"></TD><TD>(stop time)</TD>
</TR>
<TR>
<TD>dt</TD><TD><INPUT TYPE="text" NAME="dt" SIZE=15 VALUE="0.05"></TD><TD>(time step)</TD>
</TR>
<TR>
<TD>case</TD><TD><INPUT TYPE="text" NAME="case" SIZE=15 VALUE="tmp1"></TD><TD>(case name)</TD>
</TR>
<TR>
<TD>screenplot</TD><TD><INPUT TYPE="checkbox" NAME="screenplot" VALUE="1">&nbsp; <BR>
</TD><TD>(plot on the screen?)</TD>
</TR>

</TABLE><BR>
<INPUT TYPE="submit" VALUE="simulate and visualize" NAME="sim">
</FORM>

<IMG SRC="tmp1/tmp_1477.80293142.png">

</BODY></HTML>

CPU time of tmp.sh: 0.8 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running tmp.sh 
Content-type: text/html


<HTML><BODY BGCOLOR="white">
<IMG SRC="../../../misc/figs/simviz.xfig.gif" ALIGN="right"><P>
<FORM ACTION="wrapper.sh.cgi?s=simviz1cpCGI_unit.py.cgi" METHOD="POST">
<TABLE>
<TR>
<TD>m</TD><TD><INPUT TYPE="text" NAME="m" SIZE=15 VALUE="1.0"></TD><TD>kg</TD><TD>(mass)</TD>
</TR>
<TR>
<TD>b</TD><TD><INPUT TYPE="text" NAME="b" SIZE=15 VALUE="0.7"></TD><TD>kg/s</TD><TD>(damping)</TD>
</TR>
<TR>
<TD>c</TD><TD><INPUT TYPE="text" NAME="c" SIZE=15 VALUE="5.0"></TD><TD>kg/s**2</TD><TD>(stiffness)</TD>
</TR>
<TR>
<TD>func</TD><TD><SELECT NAME="func" SIZE=1 VALUE="y">
<OPTION VALUE="y">y </OPTION>
</SELECT><BR>
</TD><TD></TD><TD>(spring model function)</TD>
</TR>
<TR>
<TD>A</TD><TD><INPUT TYPE="text" NAME="A" SIZE=15 VALUE="5.0"></TD><TD>N</TD><TD>(forced amplitude)</TD>
</TR>
<TR>
<TD>w</TD><TD><INPUT TYPE="text" NAME="w" SIZE=15 VALUE="6.28318530718"></TD><TD>1/s</TD><TD>(forced frequency)</TD>
</TR>
<TR>
<TD>y0</TD><TD><INPUT TYPE="text" NAME="y0" SIZE=15 VALUE="0.2"></TD><TD>m</TD><TD>(initial displacement)</TD>
</TR>
<TR>
<TD>tstop</TD><TD><INPUT TYPE="text" NAME="tstop" SIZE=15 VALUE="30.0"></TD><TD>s</TD><TD>(stop time)</TD>
</TR>
<TR>
<TD>dt</TD><TD><INPUT TYPE="text" NAME="dt" SIZE=15 VALUE="0.05"></TD><TD>s</TD><TD>(time step)</TD>
</TR>
<TR>
<TD>case</TD><TD><INPUT TYPE="text" NAME="case" SIZE=15 VALUE="tmp1"></TD><TD></TD><TD>(case name)</TD>
</TR>
<TR>
<TD>screenplot</TD><TD><INPUT TYPE="checkbox" NAME="screenplot" VALUE="1">&nbsp; <BR>
</TD><TD></TD><TD>(plot on the screen?)</TD>
</TR>

</TABLE><BR>
<INPUT TYPE="submit" VALUE="simulate and visualize" NAME="sim">
</FORM>


</BODY></HTML>

Content-type: text/html


<HTML><BODY BGCOLOR="white">
<IMG SRC="../../../misc/figs/simviz.xfig.gif" ALIGN="right"><P>
<FORM ACTION="wrapper.sh.cgi?s=simviz1cpCGI_unit.py.cgi" METHOD="POST">
<TABLE>
<TR>
<TD>m</TD><TD><INPUT TYPE="text" NAME="m" SIZE=15 VALUE="1.0"></TD><TD>kg</TD><TD>(mass)</TD>
</TR>
<TR>
<TD>b</TD><TD><INPUT TYPE="text" NAME="b" SIZE=15 VALUE="0.7"></TD><TD>kg/s</TD><TD>(damping)</TD>
</TR>
<TR>
<TD>c</TD><TD><INPUT TYPE="text" NAME="c" SIZE=15 VALUE="5.0"></TD><TD>kg/s**2</TD><TD>(stiffness)</TD>
</TR>
<TR>
<TD>func</TD><TD><SELECT NAME="func" SIZE=1 VALUE="y">
<OPTION VALUE="y">y </OPTION>
</SELECT><BR>
</TD><TD></TD><TD>(spring model function)</TD>
</TR>
<TR>
<TD>A</TD><TD><INPUT TYPE="text" NAME="A" SIZE=15 VALUE="5.0"></TD><TD>N</TD><TD>(forced amplitude)</TD>
</TR>
<TR>
<TD>w</TD><TD><INPUT TYPE="text" NAME="w" SIZE=15 VALUE="6.28318530718"></TD><TD>1/s</TD><TD>(forced frequency)</TD>
</TR>
<TR>
<TD>y0</TD><TD><INPUT TYPE="text" NAME="y0" SIZE=15 VALUE="0.2"></TD><TD>m</TD><TD>(initial displacement)</TD>
</TR>
<TR>
<TD>tstop</TD><TD><INPUT TYPE="text" NAME="tstop" SIZE=15 VALUE="30.0"></TD><TD>s</TD><TD>(stop time)</TD>
</TR>
<TR>
<TD>dt</TD><TD><INPUT TYPE="text" NAME="dt" SIZE=15 VALUE="0.05"></TD><TD>s</TD><TD>(time step)</TD>
</TR>
<TR>
<TD>case</TD><TD><INPUT TYPE="text" NAME="case" SIZE=15 VALUE="tmp1"></TD><TD></TD><TD>(case name)</TD>
</TR>
<TR>
<TD>screenplot</TD><TD><INPUT TYPE="checkbox" NAME="screenplot" VALUE="1">&nbsp; <BR>
</TD><TD></TD><TD>(plot on the screen?)</TD>
</TR>

</TABLE><BR>
<INPUT TYPE="submit" VALUE="simulate and visualize" NAME="sim">
</FORM>

<IMG SRC="tmp1/tmp_442.621007294.png">

</BODY></HTML>

CPU time of tmp.sh: 0.8 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running mloop4simviz1.py -m '10 & 1 & 2' -c ' 0.5 & [1:6,1] & 10.1' -noscreenplot
[5, 0.5, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 1, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 2, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 3, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 4, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 5, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 6, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 10.1, 0.69999999999999996, 'y', 10, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 0.5, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 1, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 2, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 3, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 4, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 5, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 6, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 10.1, 0.69999999999999996, 'y', 1, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 0.5, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 1, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 2, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 3, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 4, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 5, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 6, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
[5, 10.1, 0.69999999999999996, 'y', 2, 6.2831853071795862, 30, 0.20000000000000001, 0.050000000000000003]
-A 5 -c 0.5 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 1 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 2 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 3 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 4 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 5 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 6 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 10.1 -b 0.69999999999999996 -func 'y' -m 10 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 0.5 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 1 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 2 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 3 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 4 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 5 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 6 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 10.1 -b 0.69999999999999996 -func 'y' -m 1 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 0.5 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 1 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 2 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 3 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 4 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 5 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 6 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
-A 5 -c 10.1 -b 0.69999999999999996 -func 'y' -m 2 -w 6.2831853071795862 -tstop 30 -y0 0.20000000000000001 -dt 0.050000000000000003
[0.5, 10] 0.1024
[1, 10] 0.1251
[2, 10] 0.1029
[3, 10] 0.1098
[4, 10] 0.1201
[5, 10] 0.1282
[6, 10] 0.1293
[10.1, 10] 0.1223
[0.5, 1] 0.1285
[1, 1] 0.1299
[2, 1] 0.1335
[3, 1] 0.1371
[4, 1] 0.1418
[5, 1] 0.1452
[6, 1] 0.1504
[10.1, 1] 0.1706
[0.5, 2] 0.0683
[1, 2] 0.0785
[2, 2] 0.0759
[3, 2] 0.0842
[4, 2] 0.0792
[5, 2] 0.0833
[6, 2] 0.0775
[10.1, 2] 0.0861
CPU time of mloop4simviz1.py: 4.9 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running mloop4simviz1_v2.py -m '10 & 1 & 2' -c ' 0.5 & [1:6,1] & 10.1' -noscreenplot
[0.5, 10] 0.1024
[1, 10] 0.1251
[2, 10] 0.1029
[3, 10] 0.1098
[4, 10] 0.1201
[5, 10] 0.1282
[6, 10] 0.1293
[10.1, 10] 0.1223
[0.5, 1] 0.1285
[1, 1] 0.1299
[2, 1] 0.1335
[3, 1] 0.1371
[4, 1] 0.1418
[5, 1] 0.1452
[6, 1] 0.1504
[10.1, 1] 0.1706
[0.5, 2] 0.0683
[1, 2] 0.0785
[2, 2] 0.0759
[3, 2] 0.0842
[4, 2] 0.0792
[5, 2] 0.0833
[6, 2] 0.0775
[10.1, 2] 0.0861
CPU time of mloop4simviz1_v2.py: 4.9 seconds on hplx30 i686, Linux


#### Test: ./tests.verify running mloop4simviz1_v3.py -m '10 & 1 & 2' -c ' 0.5 & [1:6,1] & 10.1' -noscreenplot -remove 'm == 10 and c == 2'
replace "A" by "5"
replace "c" by "0.5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "2"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "3"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "4"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "6"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "10.1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "10"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "0.5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "2"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "3"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "4"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "6"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "10.1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "1"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "0.5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "2"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "3"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "4"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "5"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "6"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
replace "A" by "5"
replace "c" by "10.1"
replace "b" by "0.69999999999999996"
replace "func" by "'y'"
replace "m" by "2"
replace "w" by "6.2831853071795862"
replace "tstop" by "30"
replace "y0" by "0.20000000000000001"
replace "dt" by "0.050000000000000003"
1 experiments removed
[0.5, 10] 0.1024
[1, 10] 0.1251
[3, 10] 0.1098
[4, 10] 0.1201
[5, 10] 0.1282
[6, 10] 0.1293
[10.1, 10] 0.1223
[0.5, 1] 0.1285
[1, 1] 0.1299
[2, 1] 0.1335
[3, 1] 0.1371
[4, 1] 0.1418
[5, 1] 0.1452
[6, 1] 0.1504
[10.1, 1] 0.1706
[0.5, 2] 0.0683
[1, 2] 0.0785
[2, 2] 0.0759
[3, 2] 0.0842
[4, 2] 0.0792
[5, 2] 0.0833
[6, 2] 0.0775
[10.1, 2] 0.0861
CPU time of mloop4simviz1_v3.py: 4.7 seconds on hplx30 i686, Linux

