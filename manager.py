# -*- coding: utf-8 -*-
_build = '075'
import urllib
from variables import check
print('checking for internet')
if check.check() is True:
    choice = input('(w)eb update or (p)eertopeer update?: ')
    if choice == 'p':
        second = input('(s)end or (r)eceive?: ')
        if second == 'r':
            files = ['main', 'variables', 'manager']
            import socket, hashlib
            s = socket.socket()
            s.bind((socket.gethostname(), 5004))
            for x in files:
                f = open('{}.py'.format(x), 'wb')
                s.listen(5)
                while True:
                    c, addr = s.accept()
                    print('Got connection for {} from {}'.format(x, addr))
                    print('Receiving {}...'.format(x))
                    l = c.recv(1024)
                    while (l):
                        f.write(l)
                        l = c.recv(1024)
                    f.close()
                    print('Done Receiving {}'.format(x))
                    c.close()
                    break
        if second == 's':
            files = ['main', 'variables', 'manager']
            import socket
            s = socket.socket()
            s.connect((socket.gethostname(), 5004))
            for x in files:
                f = open('{}.py'.format(x), 'rb')
                print('Sending {}...'.format(x))
                l = f.read(1024)
                while (l):
                    s.send(l)
                    l = f.read(1024)
                f.close()
                print('Done Sending {}'.format(x))
            s.shutdown(socket.SHUT_WR)
            print(s.recv(1024))
            s.close
    print('checking for updates')
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/main.py'
    urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    try:
        m = open('main.py')
        other = m.read()
        m.close()
    except OSError:
        words[34:37] = '000'
    if int(words[34:37]) > int(other[34:37]):
        urllib.request.urlretrieve(l, 'main.py')
        print('Main updated from b{} to b{}'.format(other[34:37], words[34:37]))
    elif int(words[34:37]) < int(other[34:37]):
        print('(DEV) Update GitHub for main (b{} to b{})'.format(words[34:37], other[34:37]))
    else:
        print('Main up to date (b{})'.format(other[34:37]))
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/variables.py'
    urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    try:
        m = open('variables.py')
        other = m.read()
        m.close()
    except OSError:
        words[34:37] = '000'
    if int(words[34:37]) > int(other[34:37]):
        urllib.request.urlretrieve(l, 'variables.py')
        print('Variables updated from b{} to b{}'.format(other[34:37], words[34:37]))
    elif int(words[34:37]) < int(other[34:37]):
        print('(DEV) Update GitHub for variables (b{} to b{})'.format(words[34:37], other[34:37]))
    else:
        print('Variables up to date (b{})'.format(other[34:37]))
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/manager.py'
    urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    if int(words[34:37]) > int(_build):
        urllib.request.urlretrieve(l, 'manager.py')
        print('Manager updated from b{} to b{}'.format(_build, words[34:37]))
        exec(open('manager.py').read())
    elif int(words[34:37]) < int(_build):
        print('(DEV) Update GitHub for manager (b{} to b{})'.format(words[34:37], _build))
    else:
        print('Manager up to date (b{})'.format(_build))
    input('Enter to boot pyos')
else:
    print('no internet')
exec(open('main.py').read())
