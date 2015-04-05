from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="post" action="parsing_get.wsgi">
      <p>
         Your hello : <input type="text" name="hello">
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Hello: %s<br>
      </p>
   </body>
</html>"""
def application(environ, start_response):
   d = parse_qs(environ['QUERY_STRING'])
   hello = d.get('hello', [''])[0] # Returns the first age value.
   hello = escape(hello)
   response_body = html % (hello or 'Empty')
   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)
   return [response_body]

#    data = "Hello, World! From  GUnicorn\n"
#    #data = str(environ)
#    start_response("200 OK", [
#        ("Content-Type", "text/plain"),
#        ("Content-Length", str(len(data)))
#    ])
#    return iter([data])

