# Setup Container Locally

## Prerequisites

* Install a working Docker environment - https://www.docker.com/get-started

## Steps

## Resources to create

1. Create IAM user to create ECR repository
2. Create an Amazon ECR Respository in same region where you create your build environment and run your build
3. Add policy to AWS CodeBuild service role to allow CodeBuild to upload Docker images to Amazon ECR repositories
4. Create docker directory and files and upload to S3 or AWS CodeCommit repo. If into S3 zip the files inside the root directory.
5. Create project in AWS CodeBuild.
6. Confirm that CodeBuild successfully pushed the Docker image to the repository

## Build sequence

1. Commit code to CodeCommit
2. Produce a docker image as a build output
3. Push the Docker image to ECS

## Configurations

### Amazon CodeBuild

| Setting | Value |
| -- | -- |
| Operating system | Ubuntu |
| Runtime | Standard |
| Image | aws/codebuild/standard:4.0 |
| Privileged | true |
| AWS_DEFAULT_REGION | [--region-ID--] |
| AWS_ACCOUNT_ID | [--account-ID--] |
| IMAGE_TAG | Latest |
| IMAGE_REPO_NAME | [--Amazon-ECR-repo-name--] |

```AWS CLI
{
  "name": "sample-docker-project",
  "source": {
    "type": "S3",
    "location": "codebuild-region-ID-account-ID-input-bucket/DockerSample.zip"
  },
  "artifacts": {
    "type": "NO_ARTIFACTS"
  },
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:4.0",
    "computeType": "BUILD_GENERAL1_SMALL",
    "environmentVariables": [
      {
        "name": "AWS_DEFAULT_REGION",
        "value": "region-ID"
      },
      {
        "name": "AWS_ACCOUNT_ID",
        "value": "account-ID"
      },
      {
        "name": "IMAGE_REPO_NAME",
        "value": "Amazon-ECR-repo-name"
      },
      {
        "name": "IMAGE_TAG",
        "value": "latest"
      }
    ],
    "privilegedMode": true
  },
  "serviceRole": "arn:aws:iam::account-ID:role/role-name",
  "encryptionKey": "arn:aws:kms:region-ID:account-ID:key/key-ID"
}
```

## Resources

* [Creating a Simple “Fetch & Run” AWS Batch Job](https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/)
