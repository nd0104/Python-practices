__author__ = 'ND'
db = {}
def newuser():
    prompt = 'login desired([q] to quit):'
    while True:
        name = raw_input(prompt)
        if name == 'q':
            break
        if db.has_key(name):
            prompt = 'name taken, try another:'
            continue
        else:
            pwd = raw_input('password:')
            db[name] = pwd
def olduser():
    name = raw_input('Login:')
    if db.has_key(name):
        pwd = raw_input('password:')
        password = db.get(name)
        if password == pwd:
            print 'Welcome back'
        else:
            print 'Incorrect password:'
    else:
        print 'No such user name'
CMDs = {'n': newuser, 'e': olduser}
def showmenu():
    prompt = """
(N)ew user
(E)xisting user login
(Q)uit
Enter choice :"""
    done = False
    while not done:
        try:
            choice = raw_input(prompt)
            if len(choice) > 0:
                choice = choice.strip()[0].lower()
        except (EOFError,KeyboardInterrupt):
            choice = 'q'
        print "you pick: [%s]" % choice
        if choice not in 'neq' or len(choice) < 1:
            print 'invalid option, try again'
        else:
            if choice == 'q':
                done = True
            CMDs[choice]()


if __name__ == '__main__':
    showmenu()
















