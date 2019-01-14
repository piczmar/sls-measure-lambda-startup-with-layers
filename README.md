
# Measuring lambda cold and hot startup time with and without layer.

It is based on [another project](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats) 
which contains 4 branches dedicated to measure lambda startup: 
 - [cold with layer](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats/tree/measure-startup-layer-cold)
 - [cold without layer](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats/tree/measure-startup-nolayer-cold)
 - [hot with layer](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats/tree/measure-startup-layer-hot)
 - [hot without layer](https://github.com/piczmar/sls-aws-java-github-webhook-gitstats/tree/measure-startup-layer-hot)

To gather measures each of the 4 projects need to be deployed in AWS.
There is a `setup.sh` script to automate it. It will clone each branch, then build and deploy it.

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
aws dynamodb scan --profile sls --region us-east-1 --table-name aws-java-github-webhook-lcold-dev-stats  --query "Items[*].[duration.N,timestamp.N]" --output text > layer-cold.txt
aws dynamodb scan --profile sls --region us-east-1 --table-name aws-java-github-webhook-lhot-dev-stats  --query "Items[*].[duration.N,timestamp.N]" --output text > layer-hot.txt
aws dynamodb scan --profile sls --region us-east-1 --table-name aws-java-github-webhook-nolcold-dev-stats  --query "Items[*].[duration.N,timestamp.N]" --output text > nolayer-cold.txt
aws dynamodb scan --profile sls --region us-east-1 --table-name aws-java-github-webhook-nolhot-dev-stats  --query "Items[*].[duration.N,timestamp.N]" --output text > nolayer-hot.txt
```

Then all txt files were printed on chart using Python Plotly library.

I used Anaconda environment for this: 
```
conda create -n plotly python=3.6 pandas plotly
conda activate plotly
python print-dynamo-data-combined.py
python boxes.py
```

[data/print-dynamo-data-combined.py](data/print-dynamo-data-combined.py) - prints a [timeline chart](http://htmlpreview.github.io/?https://github.com/piczmar/sls-measure-lambda-startup-with-layers/blob/master/data/timeline-plot.html)

[data/boxes.py](data/boxes.py) - prints a [box chart](http://htmlpreview.github.io/?https://github.com/piczmar/sls-measure-lambda-startup-with-layers/blob/master/data/boxes-plot.html)


I recorded a screen cast and converted movies to gifs with `ffmpeg` and `gifsicle` like that: 

```
ffmpeg -i nl-l-cold.mov -s 1400x800 -pix_fmt rgb24 -r 20 -f gif -  | gifsicle --optimize=3 --delay=3 > nl-l-cold.gif
```

The results were described in [this]() blog post
