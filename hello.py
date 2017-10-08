from urllib.parse import parse_qs as parser


bind = "0.0.0.0:8080"


def app(environ, start_response):
    """Simplest possible application object"""
#    resp = parser(environ['QUERY_STRING'])
    data = '\n'.join(environ.get('QUERY_STRING').split('&'))
    print(str(data))
    print(str(len(data)))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [data.encode('utf-8')]
