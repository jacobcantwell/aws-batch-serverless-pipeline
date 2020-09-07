import json
import boto3
import pprint
#initialize
pp = pprint.PrettyPrinter(indent=4)
def lambda_handler(event, context):
    '''
    triggers a step function from the S3 landing event, 
    passing along the S3 file info
    '''
    print(event)
    #Fallback tests for initializations outside scope
    try:
        pp
    except NameError:
        pp = pprint.PrettyPrinter(indent=4)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    input= {
        'bucket_name': bucket_name,
        'file_key': file_key
    }     
    print(input)
    stepFunction = boto3.client('stepfunctions')
    response = stepFunction.start_execution(
        stateMachineArn='<STEP_FUNCTION_STATE_MACHINE_ARN>',
        input = json.dumps(input, indent=4)
    )
    return pp.pprint(response)