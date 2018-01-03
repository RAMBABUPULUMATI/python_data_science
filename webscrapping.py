import urllib.request
import urllib.parse
import re

count = 1
name = 'angela'
while count < 50:
    if count == 1:
        url = '<use your own url>'
    else:
        url = '<use your own url>'
    values = {'s': '< search criteria>', 'submit': 'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    paragraphs = re.findall(r'<any search criteria for regular expression >', str(respData))
    for eachp in paragraphs:
 #       if eachp[0].__len__() >= 8:
  #          if any(c.isupper() for c in eachp[0]):
       print(eachp[0])
    count += 1
