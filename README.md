
Measuring lambda cold and hot startup time with and without layer.

It is based on [another project](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats) 
which contains 4 branches dedicated to measure lambda startup: 
 - cold with layer
 - cold without layer
 - hot with layer
 - hot without layer

To gather measures each of the 4 projects need to be deployed.
There is a `setup.sh` script to automate it.

Based on [this benchmark](https://read.acloud.guru/how-long-does-aws-lambda-keep-your-idle-functions-around-before-a-cold-start-bf715d3b810) 
I assumed 1h as a sufficient interval for triggering cold startup of Lambda function.

Each project will deploy 3 lambdas: 
 - a cron function scheduled to trigger another function on time interval (1h for cold start and 2 min for hot start measures)
 - a lambda which will trigger another lambda asynchronously, hence it does not include any logic apart from that
 - a lambda triggered asynchronously and doing some computation, but it is only because I reused my existing project. It has no impact on measurements.

All lambdas are deployed in the same region to minimize network latency during the measures.

The Cron lambda will store duration of invocation of another lambda in DynamoDB table of schema: 
- Duration - duration of lambda execution in milliseconds
- Timestamp - timestamp of cron invocation in milliseconds

After some time when the measures were gathered in database the data
was exported to txt file with aws CLI like: 

```
aws dynamodb scan --profile sls --region us-east-1 --table-name aws-java-github-webhook-nolayers-dev-stats  --query "Items[*].[duration.N,timestamp.N]" --output text > no-layer.txt

```

Then all txt files were printed on chart using Python Plotly library.

I used Anaconda environment like this: 
```
conda create -n plotly python=3.6 pandas plotly
conda activate plotly
python print-dynamo-data-combined.py
```

