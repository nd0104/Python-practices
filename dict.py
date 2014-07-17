__author__ = 'ND'
people = {'Jack':{'phone':'138','addr':'Foo Diver 23'},
          'Benth':{'phone':'139','addr':'CHengdu'},
          'Lily':{'phone':'189','addr':'Beijing'}
}

labels = {'phone':'phone number','addr':'address'}
name = raw_input('plz input the name:')
request = raw_input('Phone number(p) or address(a)?')
if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

if name in people:
    print "%s'%s is %s" % (name,labels[key],people[name][key])