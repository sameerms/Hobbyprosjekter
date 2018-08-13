#!/local/gnu/bin/bash
# usage: www.some.net/url/wrapper.sh.cgi?s=myCGIscript.py

# set environment variables:
export PATH=/usr/bin:/bin:/local/snacks/bin
root=/hom/inf3330/www_docs
export scripting=$root/scripting
export MACHINE_TYPE=`uname`
export SYSDIR=$root/packages
BIN1=$SYSDIR/$MACHINE_TYPE
BIN2=$scripting/$MACHINE_TYPE
export LD_LIBRARY_PATH=$BIN1/lib:/usr/bin/X11/lib
PATH=$BIN1/bin:$BIN2/bin:$scripting/src/tools:$PATH:/local/bin
export PYTHONPATH=$SYSDIR/src/python/tools:$scripting/src/tools

# extract CGI script name from QUERY_STRING:
script=`python -c "print '$QUERY_STRING'.split('=')[1]"`

# run the script:
#python $script   # not recommended of security reasons (can run _any_ py file)
./$script         # run file in current directory
