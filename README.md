# qrcode-decode-server

# Requirement
```
$ sudo yum install zbar-devel.x86_64
$ pip install Pillow
$ pip install zbarlight
$ pip install flask
$ pip install tornado
```


# Run
```
$ python server.py
```


# Test
```
$ curl -XGET 'http://localhost'
```

```
$ curl -XPOST 'http://localhost/decode' -d '{"url": "http://aaa.com/bbb/qrcode.png"}'
```
