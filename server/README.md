# 服务器

## 运行

如果还没有安装flask，请运行以下命令

```bash
pip install Flask
```

安装后，在命令行运行

```bash
cd server
python app.py
```

## Http 接口文档

使用以下python代码向服务器发送请求
```python
import http.client

conn = http.client.HTTPConnection('localhost:80') # 按需改变主机
conn.request('POST', '<url>', '<data>') # url和data的用法请看下文
conn.getresponse()

```

### 语音模块

```python
import http.client

conn = http.client.HTTPConnection('localhost:80') # 按需改变主机
conn.request('POST', '/voice', '${content}') # content 是 voice_control.py 里面的串口发送内容
conn.getresponse() # 可选，由于调试
```

### 图像识别

```python
import http.client

conn = http.client.HTTPConnection('localhost:80') # 按需改变主机
conn.request('POST', '/track', '${content}') # content 是 track.py 里面的串口发送内容
conn.getresponse() # 可选，由于调试
```
