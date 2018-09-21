# hq-lambda-api-python
This is a python implementation of the AWS Lambda functions and API Gateway that will be accessed by the HQ Trivia Assistant DialogFlow agent. 

The code here is thus used only in an AWS-based configured of the application backend.

## Usage

This repo is the one that is accessed by the CodeBuild project in pipeline.yaml within **hq-cloudformation-templates**. As such there is no set-up process per se, as it this is handled during the creation of the CloudFormation stack. No additional resources need to be created, other than the ones provisioned in the CloudFormation template. 

The CodeBuild project is specifically designed to pull from the tip of the **master** branch of this repo, whenever it is updated. Thus any change to **any** file of the the master branch will result in a new build process being kicked off within the CodePipeline project on AWS. 

Note that the Github user embedded in the pipeline.yaml file in **hq-cloudformation-templates** needs to have authenticated READ access to *this* repo in order for the pipeline to access the source files here, and to create/update the Lambda functions.

Note as well that the **buildspec.yaml** in this repo is *not* used by CodeBuild, but is bypassed by an embedded build script within pipeline.yaml (this is done in order to provide proper substitution of parameter variables in the build script, which should only be done at the time that the CloudFormation template is run. The buildspec.yaml is provided here only as a reference in such case, and may not reflect the actual build process as configured in the CodePipeline project.

## Usage of API

This is the temporary API for development. It can be used for simple testing of end to end. 

Note this WILL change at some point, even during testing, so I'll be providing updated docs as need. In particular the hashed unique id part of the AWS domain name (e.g. 6d9kid0a9) will change, and also 'Stage' will become 'Prod' at some point. 

We may of course need other calls depending on other client requirements that may pop up. So long as we're collecting the right data along the way and storing it properly, we should find it fairly straightforward to give stats and comparisons by other operations.

For testing, the two POST calls, for now simply send a body as a serialized json object of the params{ userId : 1, sessionId: 2}.

For the GET call, add query string as normal, i.e. 
?userId=1&sessionId=2. 

Param values are arbitrary for more. Params are actually more extensive than this for the POST calls, but since nothing is implemented in db for now, don't worry about others, or the values of the ones you send (i.e. can use dummy values for params for now).

POST https://c6d9kid0a9.execute-api.us-west-2.amazonaws.com/Stage/StartNewQuiz

POST https://c6d9kid0a9.execute-api.us-west-2.amazonaws.com/Stage/SaveQuestionResponse

GET https://c6d9kid0a9.execute-api.us-west-2.amazonaws.com/Stage/GetQuizScore 

.



