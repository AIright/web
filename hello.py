from urllib.parse import parse_qs as parser


bind = "0.0.0.0:8080"


def app(environ, start_response):
    """Simplest possible application object"""
    resp = parser(environ['QUERY_STRING'])
    data = ''
    for a in resp:
        for b in resp.get(a):
            data = data + '{0}={1}\n'.format(a, b)

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data.encode('utf-8')])
