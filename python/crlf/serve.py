'''
    Simple example of what happens to applications vulnerable to CRLF injections.
    CR = \r
    LF = \n

    Attacker is able to inject HTTP headers OR add content by using a double CRLF
'''

import sys

vulnerable_host = 'https://www.vulnerable-app.com'
hacker_host = 'http://evil-hacker.com'

def make_request(payload=''):
    http_request = f'''
        \rGET / HTTP/1.1
        \r\nHost: {vulnerable_host}/{payload}
    '''
    print(http_request)
    return 0


if len(sys.argv) < 1:
    print('No payload used')
    make_request()
else:
    make_request(sys.argv[1])


