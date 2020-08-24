# -*- coding: utf-8 -*-
_build = '110'
try:
    print('loading pre-log necessaries')
    import time, os
    starttime = time.time()
    print('loading os')
    import os
    print('loading sys')
    import sys
    with open('log', 'w') as n:
        n.write('')
    n = open('log', 'a+')
    n.write('started manager log\n')
    k = 'loading modules'
    print(k)
    n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
    import urllib
    n.write('[{:.8f}] status: urllib loaded\n'.format(time.time() - starttime))
    import platform
    n.write('[{:.8f}] status: platform loaded\n'.format(time.time() - starttime))
    import subprocess
    n.write('[{:.8f}] status: subprocess loaded\n'.format(time.time() - starttime))
    from imports import check
    n.write('[{:.8f}] status: imports.check loaded\n'.format(time.time() - starttime))
    k = 'checking for internet'
    print(k)
    n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
    if check.check() is True:
        n.write('[{:.8f}] status: check.check() successful\n'.format(time.time() - starttime))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/README'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for readme\n'.format(time.time() - starttime))
        urllib.request.urlretrieve(l, 'README')
        k = 'got README'
        print(k)
        n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/LICENSE'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for license\n'.format(time.time() - starttime))
        urllib.request.urlretrieve(l, 'LICENSE')
        k = 'got LICENSE'
        print(k)
        n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
        k = 'checking for updates'
        print(k)
        n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/data'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for data check\n'.format(time.time() - starttime))
        try:
            m = open('data', 'r')
            m.close()
            n.write('[{:.8f}] status: successfully read data\n'.format(time.time() - starttime))
            print('data exists')
        except OSError:
            n.write('[{:.8f}] status: failed to read data, downloading\n'.format(time.time() - starttime))
            urllib.request.urlretrieve(l, 'data')
            k = 'data downloaded'
            print(k)
            n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/main.py'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for main.py update\n'.format(time.time() - starttime))
        r = open('cache', 'r')
        w = r.read()[34:37]
        r.close()
        n.write('[{:.8f}] status: successfully read cache\n'.format(time.time() - starttime))
        try:
            m = open('main.py', 'r')
            o = m.read()[34:37]
            m.close()
            n.write('[{:.8f}] status: successfully read main.py\n'.format(time.time() - starttime))
        except OSError:
            o = '000'
            n.write('[{:.8f}] status: failed to read main.py, setting _build to 000\n'.format(time.time() - starttime))
        if int(w) > int(o):
            urllib.request.urlretrieve(l, 'main.py')
            k = 'main updated from b{} to b{}'.format(o, w)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        elif int(w) < int(o):
            k = 'update github for main (b{} to b{})'.format(w, o)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        else:
            k = 'main up to date (b{})'.format(o)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/imports.py'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for imports.py update\n'.format(time.time() - starttime))
        r = open('cache', 'r')
        w = r.read()[34:37]
        r.close()
        n.write('[{:.8f}] status: successfully read cache\n'.format(time.time() - starttime))
        try:
            m = open('imports.py', 'r')
            o = m.read()[34:37]
            m.close()
            n.write('[{:.8f}] status: successfully read imports.py\n'.format(time.time() - starttime))
        except OSError:
            o = '000'
            n.write('[{:.8f}] status: failed to read imports.py, setting _build to 000\n'.format(time.time() - starttime))
        if int(w) > int(o):
            urllib.request.urlretrieve(l, 'imports.py')
            k = 'imports updated from b{} to b{}'.format(o, w)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        elif int(w) < int(o):
            k = 'update github for imports (b{} to b{})'.format(w, o)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        else:
            k = 'imports up to date (b{})'.format(o)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/updater.py'
        urllib.request.urlretrieve(l, 'cache')
        n.write('[{:.8f}] status: got url for updater.py update\n'.format(time.time() - starttime))
        r = open('cache', 'r')
        w = r.read()[34:37]
        r.close()
        n.write('[{:.8f}] status: successfully read updater.py\n'.format(time.time() - starttime))
        if int(w) > int(_build):
            urllib.request.urlretrieve(l, 'updater.py')
            k = 'updater updated from b{} to b{}'.format(_build, w)
            print(k)
            n.write('[{:.8f}] updater: {}; restarting\n'.format(time.time() - starttime, k))
            print('restarting updater')
            exec(open('updater.py', 'r').read())
        elif int(w) < int(_build):
            k = 'update github for updater (b{} to b{})'.format(w, _build)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        else:
            k = 'updater up to date (b{})'.format(_build)
            print(k)
            n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
        k = 'total runtime: {:.8f}'.format(time.time() - starttime)
        print(k)
        n.write('[{:.8f}] updater: {}\n'.format(time.time() - starttime, k))
    else:
        k = 'no internet'
        print(k)
        n.write('[{:.8f}] status: check.check() unsuccessful\n'.format(time.time() - starttime))
    input('enter to boot pyos')
    term = 'cls'
    if platform.system() == 'Linux':
        term = 'clear'
    tmp = subprocess.call(term, shell=True)
    n.write('[{:.8f}] updater: terms loaded, screen cleared\n'.format(time.time() - starttime))
    n.write('[{:.8f}] updater: pyos booted\n'.format(time.time() - starttime))
    n.close()
    exec(open('main.py', 'r').read())
except Exception as err:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
