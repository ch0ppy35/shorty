# Shorty, the serverless link shortener

This is a serverless implementation of my [pyTinifier](https://github.com/mmillerlevels/pyTinifier) app I build a while back in Flask.

This isn't a monolith, so it's more efficiant!

## Todo

- ~~This is purely an api right now. Need to get a UI for this yet.~~
- Need to get this plugged into cloudwatch (UI/API)
- ~~Fix a packaging issue. In Lambda, the funtions are getting all files; not just handlers and reqs...~~
- Stop using `time` and `datetime` in the create handler.  No need for that...Lol.

## Requirements

- An AWS account (Make sure you've got your creds configured on your machine)
- Have the serverless framework installed `npm install -g serverless`
- Run `npm install serverless-python-individually` you'll need this too for this implementation

## Example Use

```
$ curl -XPOST -H "Content-Type: application/json" https://shorty.mikemiller.tech/create -d '{"original_url": "https://www.serverless.com/"}'  
{"short_url": "https://shorty.mikemiller.tech/u/1Ki0MT"}
```

```
$ curl -i https://shorty.mikemiller.tech/u/1Ki0MT
HTTP/2 301 
date: Tue, 15 Sep 2020 02:34:05 GMT
content-type: application/json
content-length: 0
location: https://www.serverless.com/
x-amzn-requestid: 62504982-ef36-4360-bdde-e08fc6c777be
x-amz-apigw-id: S4s0lEeLvHcF68Q=
x-amzn-trace-id: Root=1-5f60281d-c1f80ca891316c842d4dcc77;Sampled=0
```
