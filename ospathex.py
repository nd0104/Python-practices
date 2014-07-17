__author__ = 'ND'
import os
for tmpdir in ('/tmp',r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no temp directory available'
        tmpdir = ''
if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd
    print '*** creating example dirctory'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new directory'
    print cwd
    print '*** original directory listing'
    print os.listdir(cwd)

    print '***creating example file'
    fobj = open('test','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** updated directory listing'
    print os.listdir(cwd)

    os.rename('test','file.txt')
    print os.listdir(cwd)

    path = os.path.join(cwd,os.listdir(cwd)[0])
    print path
    print '*** (pathname,basename)=='
    print os.path.split(path)
