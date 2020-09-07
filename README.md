# AWS Batch and AWS Step Functions

This architecture decouples the batch engine and workflow orchestration.

* Workflow creation is defined in JSON and can also integrate with non-AWS Batch applications
* Array jobs in AWS Batch support the capability to fan-out individual steps along with support for job dependency models.
* AWS Batch supports dynamic compute provisioning and scaling, so we could provision 10 jobs or 10,000 jobs without paying for idle time for the resources.

## Considerations

### Considerations for Batch Layer

* Data Sharing: Jobs are managed at the container, not instance level, so cannot guarantee containers in a workflow will run on the same instance. Stage all data in Amazon S3, and read and write everything from there. This is also important for traceability, logging, and debugging.
* Multitenancy: Maybe have multiple containers running batch processes on the same instance in same base working directory. Within scratch directory, each batch process creates a subfolder with a unique ID. All scratch data written to this subdirectory.
* Volume Reuse: Scratch data should live only as long as the job using it in order to optimize for instance and Amazon EBS storage costs. Within scratch directory, each batch process creates a subfolder with a unique ID. Delete subdirectory at end of job.

## Sequence

1. [Setup Container Locally](setup-container-locally.md)
2. [Setup Container Build Pipeline](setup-container-build-pipeline.md)
3. [Setup AWS Batch](setup-aws-batch.md)
4. [Setup AWS Step Functions](setup-aws-step-functions.md)
5. [Setup AWS Lambda Functions](setup-aws-lambda-functions.md)
