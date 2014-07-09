__author__ = 'ND'
import string
alphas = string.letters + '_'
nums = string.digits

inp = raw_input('>')
print alphas
if len(inp) > 1:
    if inp[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphas + nums:
                    print '''invalid: remaining
                                        symbols must be alphabetic'''
                    break
            else:
                print "Ok"