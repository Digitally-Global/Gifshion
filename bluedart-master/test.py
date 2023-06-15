import requests

xml = """
  <?xml version='1.0' encoding='utf-8'?>
  <a>6</a>
  """
headers = {'Content-Type': 'application/xml'} # set what your server accepts
print(requests.post('http://httpbin.org/post', data=xml, headers=headers))