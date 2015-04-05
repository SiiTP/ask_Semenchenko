#THIS IS GET APPLICATION
from cgi import parse_qs

html = """
<html>
<body>
   <form method="get" action="">
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
   d = parse_qs(environ['QUERY_STRING'])
   hello = d.get('hello', [''])[0]
   response_body = html % (hello or 'Empty')
   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)
   return [response_body]


