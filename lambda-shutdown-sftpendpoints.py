import boto3

def lambda_handler(event, context):
    sftpClient = boto3.client("transfer")
    sftpEndpointList = sftpClient.list_servers()

    while sftpEndpointList:
        for endpoint in sftpEndpointList['Servers']:
            noShutdown = sftpClient.list_tags_for_resource(Arn=endpoint['Arn'])
            print(noShutdown)
            if 'noShutdown' not in [t['Key'] for t in noShutdown['Tags']]:
                response = sftpClient.stop_server(ServerId=endpoint['ServerId'])
                return 200
        sftpEndpointList = sftpClient.list_servers(
            NextToken=sftpEndpointList['NextToken']) if 'NextToken' in sftpEndpointList else None