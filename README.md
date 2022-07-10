# accountclose

AWS Organizations introduced an API to close accounts.
https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html

It comes with following condition: *You can only close 10% of active member accounts within a rolling 30 day period. This quota is not bound by a calendar month, but starts when you close an account. Within 30 days of that initial account closure, you can't exceed the 10% account closure limit*

Then there combine this with the recommendation to un-manage account from Control Tower before deleting account.
https://docs.aws.amazon.com/controltower/latest/userguide/delete-account.html

This solution tackles both points, all you have to do is terminate Service Catalog provisioned product corresponding to the account and this solution listens to the event and clsoed the account using Organization account close API (as above)
It uses step function and re tries account close again incase you hit the 10% in 30 day condition (mentioned above)
https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html


## Clone the repo

```bash
git clone https://github.com/vsr2158/SAM_accountclose_controltower.git
```

## Deploy

To build and deploy your application for the first time, run the following in your shell:

```bash
cd SAM_accountclose_controltower/
sam build 
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to. This should match your ControlTower home region.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

## Cleanup

Finally to delete the application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name <>
```


