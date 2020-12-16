import http.client

conn = http.client.HTTPConnection('localhost:80') # 按需改变主机
conn.request('POST', '/voice', 'fasfsa') # content 是 voice_control.py 里面的串口发送内容
conn.getresponse()