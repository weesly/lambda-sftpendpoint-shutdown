# AWS Lambda - Shutdown sFTP Endpoint
This little lambda function will shutdown all running sFTP endpoints (AWS Transfer Service) automatically. So you can save money, if some Dev forgot to shutdown his notebook instance.

# ToDo

1. First you need to create a Lambda function
2. Create custom IAM policy (See [policy-iam.json](policy-iam.json) for mor information)
3. Create an scheduled CloudWatch Event, and use - for example `59 23 ? * MON-FRI *` as Cronjob Statement, to run the Lambda function every weekdays evening at 23:59:00 to shutdown all running endpoints.
4. Choose Lambda as target
5. Enjoy!

# Tagging

There could be the reason, not to shutdown a notebook instance. Just add the Tag `NoShutdown = true` to this notebook instance. Those instanced, who are tagged, will be ignored.