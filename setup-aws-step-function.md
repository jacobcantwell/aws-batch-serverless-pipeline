# AWS Step Functions

## Manual Instructions

### Create a compute environment

| Setting | Value |
| -- | -- |
| Compute environment type | Managed |
| Service role | Managed |

## Resources to create

1. Create AWS Step Function. See /step-functions/step-machine-alpha.asl.json for the state machine configuration.
2. Pass a json object to the Step Machine when invoking the job with the parameters for the job.
3. Test with Start Execution in the console.
4. Trigger the Step Function from another Lambda or API Gateway.

### Configuring Job

You can pass portions of the state input into parameters by using paths. A path is a string, beginning with $, that's used to identify components within JSON text. Step Functions paths use JsonPath syntax.

These are the environment parameters in JSON format that are passed to the container.

```json
{
  "comment": "A comment about this job",
  "batchjob": {
    "parameters": "foo",
    "otherInfo": "bar"
  },
  "data": "example"
}
```

You could pass the message foo as a parameter using the following.

```text
"Parameters.$": "$.batchjob.parameters",
"ContainerOverrides": {
    "Vcpus": 4
  }
```

```json
{
  "Parameters": {
    "name":"test"
  },
  "ContainerOverrides": {
    "Command": [
      "echo",
      "Ref::name"
    ]
  }
}
```

## Resources

* [Work with state machines in VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/bulding-stepfunctions.html#starting-stepfunctions)
* [Manage AWS Batch with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-batch.html)
* [Pass Parameters to a Service API](https://docs.aws.amazon.com/step-functions/latest/dg/connect-parameters.html)
* [How do I pass parameters from a scheduled trigger in CloudWatch to an AWS Batch job?](https://aws.amazon.com/premiumsupport/knowledge-center/batch-parameters-trigger-cloudwatch/)