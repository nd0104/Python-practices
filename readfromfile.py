fname = raw_input('Enter the file name >')
print

try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error***", e
else:
    for eachLine in fobj:
        print eachLine
    fobj.close()
