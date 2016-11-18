# qrcode-decode-server

![](https://github.com/hyeonjae/qrcode-decode-server/blob/master/guide.gif)

## Requirement
```
$ sudo yum install zbar-devel.x86_64
$ pip install Pillow
$ pip install zbarlight
$ pip install flask
$ pip install tornado
```


## Run
```
$ python server.py
```


## Test

### Run test
```bash
$ curl -XGET 'http://localhost'
```


### Request
```bash
$ curl -XPOST 'http://localhost/decode' -d '{"url": "https://goo.gl/vEbsWD.qr"}'
```

### Response
```json
{
  "codes": [
    "github.com/hyeonjae/qrcode-decode-server"
  ]
}
```
