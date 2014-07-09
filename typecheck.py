__author__ = 'ND'
def disp_type(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'NOT a number at all'

disp_type(-69)
disp_type(99999999999999999999999999L)
disp_type(98.6)
disp_type(-5.2+1.9j)
disp_type('xxx')

