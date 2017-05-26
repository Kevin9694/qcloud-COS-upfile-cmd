# qcloud-COS-upfile-cmd

Upload files to tencent (qcloud) COS
## setting
you should add a "config.json" first, like this:
```json
{
  "appid" : ,
  "secret_id" : "",
  "secret_key" : "",
  "region_info" : "",
  "bucketname": "",
  "bucketPath" : "http://blahblah-guruguru.costj.myqcloud.com"
}
```
all settings is used for connect with COS, except the last, which is to return the url.
