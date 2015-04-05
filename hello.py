# THIS IS POST APPLICATION
from cgi import parse_qs

html = """
<html>
<body>
   <form method="post" action="">
      <p>
         Your hello : <input type="text" name="hello">
         </p>
      <p>
         <input type="submit" value="OK">
         </p>
      </form>
   <p>
      Hello: %s<br>
      </p>
   </body>
</html>"""
def application(environ, start_response):
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0
   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)
   hello = d.get('hello', [''])[0]
   response_body = html % (hello or 'Empty')
   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)
   return [response_body]


