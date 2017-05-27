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
## introduction
There are three directions you can use by options, "-o" is for "/other/", "-s" is for "/static/" and "-a" is for "/archive/"
second and third direction is to classify the file extension just like "blah.md" will save in /document/md/blash.md or blah.py" in "/code/py/blah.py"
you can set this in fild.py

Next argument is your filepath. 
In terminal just like 
```bash
cosup -s ./blah.md
```
If upload is succeed, you will get a HTTP link to your file.