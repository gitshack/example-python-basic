def app(env, start_response):
    from pyinfo import pyinfo
    output = pyinfo()
    start_response('200 OK', [('Content-type', 'text/html')])
    return [bytes(output, 'utf-8')]
