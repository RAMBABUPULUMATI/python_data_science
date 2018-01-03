import urllib.request
import urllib.parse
import urllib.response

url = '<use any website>'
values = {'q':'<any search criteria>',
          'submit':'search'}


data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)