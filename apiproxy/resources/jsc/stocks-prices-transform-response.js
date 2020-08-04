var res = response.content.asJSON;

res.info = JSON.parse(context.getVariable("stockInfo.content"));

response.content = JSON.stringify(res, null, 2);