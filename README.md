# Shorty, the serverless link shortener

This is a serverless implementation of my [pyTinifier](https://github.com/mmillerlevels/pyTinifier) app I build a while back in Flask.

This isn't a monolith, so it's more efficiant!

## Todo

This is purely an api right now. Need to get a UI for this yet.

## Requirements

- An AWS account (Make sure you've got your creds configured on your machine)
- Have the serverless framework installed `npm install -g serverless`
- Run `npm install serverless-python-individually` you'll need this too for this implementation

## Example Use

```
$ curl -XPOST -H "Content-Type: application/json" https://shorty.mikemiller.tech/create -d '{"original_url": "https://news.google.com"}'
https://shorty.mikemiller.tech/u/1KhdEt
```

```
$ curl -i https://shorty.mikemiller.tech/u/1KhdEt
HTTP/2 301
date: Sat, 12 Sep 2020 22:06:31 GMT
content-type: application/json
content-length: 0
location: https://news.google.com
x-amzn-requestid: f2a3ac69-4773-41a0-b859-37a60f70d927
x-amz-apigw-id: SxfwIEwlvHcFc5g=
x-amzn-trace-id: Root=1-5f5d4667-d53654605da42720a908ef40;Sampled=0
```
