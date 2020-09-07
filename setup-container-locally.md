# Setup Container Locally

## Prerequisites

* Install a working Docker environment - https://www.docker.com/get-started

## Steps

## Resources to create

1. Edit the Python3 code
2. Build the Docker image
3. Push to ECR Repository

### Build the Docker image

```bash
docker build -t aws-hello-world .
docker images
docker run -t -i -p 80:80 aws-hello-world
```

### Push to ECR Repository

Inside the Amazon Container Services, follow these steps to upload your Docker image to an Amazon ECR repository.

* Create an ECR Repository
* Click in the new repository and click the button 'View push commands'

## Resources

* [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.put_item)
* [A Guide to Locally Testing Containers with Amazon ECS Local Endpoints and Docker Compose](https://aws.amazon.com/blogs/compute/a-guide-to-locally-testing-containers-with-amazon-ecs-local-endpoints-and-docker-compose/)
* [Creating a Simple “Fetch & Run” AWS Batch Job](https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/)
