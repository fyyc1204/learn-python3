import urllib, urllib2, sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=iFG8p4bOIzSfVya7hWFyWpCz&client_secret=ipIFiTams4qqyMX1YoeUbTfG5yXjoApC'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)