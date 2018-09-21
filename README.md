# hq-lambda-api-python
This is a python implementatin of the AWS Lambda functions and API Gateway that will be accessed by the HQ Trivia Assistant DialogFlow agent. 

Note that this repo is the one that is accessed by the CodeBuild project in pipeline.yaml within hq-cloudformation-templates. The Github user embedded in that file needs to have READ access to this repo.

Note as well that if the CodeBuild project that uses this repo is set-up with the pipeline.yaml template, as per the directions in the repo hq-cloudformation-templates, then the buildspec.yaml in this repo is not used, but is bypassed by an embedded buildscript within pipeline.yaml (this is done in order to provide proper substitution of parameter variables in the build script, which should only be done at the time that the CloudFormation template is run. The buildspec.yaml is provided here only as a reference in such case, and may not reflect the actual build process as configured in the CodePipeline project.

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

## Installation

### Create the S3 Bucket

Create the S3 bucket that will be used below.

### Create the IAM Role

Create necessary permissions for Pipeline to be built.

### Create the Pipeline

* Sign in to the AWS Management Console and open the AWS CodePipeline console at http://console.aws.amazon.com/codepipeline.
* On the Welcome page, choose **Create pipeline**. (If this is your first time using AWS CodePipeline, choose **Get Started Now**).
* On the **Step 1: Name page**, in Pipeline name, type **HQUTriviaApiBackend**, and then choose **Next step**.

* On the **Step 2: Source page**, in the Source provider drop-down list, choose **Github**, and then choose **Next step**.

* Choose the GitHub repository **thebrigade/hqu-trivia-api-backend** yas the source location for your pipeline. In Branch, from the drop-down list, choose the **master** branch.

* On the **Step 3: Build** page,  choose **AWS CodeBuild**.
* Choose **Create a new build project**.
* For **Application name**, type **HQUTriviaApiBackendBuild**.
* For **Environment image**, choose **Use an image managed by AWS CodeBuild**.
* For **Operating System**, choose **Ubuntu**.
* For **Runtime**, choose **Python**.
* For **Version**, choose **aws/codebuild/python:3.6.5**.
* For **Build specification**, choose **Use the buildspec.yml in the source code root directory.**
* Under **AWS CodeBuild service role**,  choose **Create role**. On the IAM console page that describes the role to be created for you, choose **Allow**. On the Step 5: Service Role page, AWS-CodePipeline-Service appears in the drop-down box
* Choose **Save build project**.
* Once build is saved, choose **Next step**.
* On the **Step 4: Deploy** page, from the **Deployment provider** drop-down list, choose **AWS CloudFormation**.
* For **Action mode**, choose **Create or replace a change set**.
* For **Stack name**, type **HQUTriviaApiBackendStack**.
* For **Change set name**, type **HQUTriviaApiBackendChangeSet**.
* For **Template file**, type **outputSamTemplate.yaml**.
* For **Capabilities**, choose **CAPABILITY_IAM**.
* For **Role name**, choose
* Choose **Next step**.

* On the **Step 5: Service Role** page,
* On the **Step 6: Review page**, choose **Create pipeline**.

### Edit Pipeline to deploy change set
* Click **Edit pipeline**.
* Click + to add a stage at the bottom of the pipeline. 
* For the name of the new action, type **HQUTriviaApiBackendChangeSet**
* Click + to add an action to this new stage.
* For **Action category** choose **Deploy**
* For **Action name**, type **HQUTriviaApiBackendDeployChangeSetAction**.
* For **Deployment provider**, choose **AWS CloudFormation**.
* For **Action mode**, choose **Execute a change set**.
* For **Stack name**, choose **HQUTriviaApiBackendStack**.
* For **Change set name**, choose **HQUTriviaApiBackendChangeSet**.
* Click **Add action**.
* At the next screen, click **Save pipeline changes**.



