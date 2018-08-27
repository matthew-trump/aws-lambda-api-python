# hqu-trivia-api-backend
This is the set of lambda functions that will be used by the DialogFlow agent in the HQU Trivia application for Google Assistant. 

## Installation

### Create the S3 Bucket

### Create the IAM Role

### Create the Pipeline

* Sign in to the AWS Management Console and open the AWS CodePipeline console at http://console.aws.amazon.com/codepipeline.
* On the Welcome page, choose **Create pipeline**. (If this is your first time using AWS CodePipeline, choose **Get Started Now**).
* On the **Step 1: Name page**, in Pipeline name, type **HQUTriviaApiBackend**, and then choose **Next step**.

* On the **Step 2: Source page**, in the Source provider drop-down list, choose **Github**, and then choose **Next step**.

* Choose the GitHub repository **thebrigade/hqu-trivia-api-backend** yas the source location for your pipeline. In Branch, from the drop-down list, choose the **master** branch.

* On the **Step 3: Build** page,  choose **AWS CodeBuild**.
* Choose **Create a new build project**.
* For **Environment image**, choose **Use an image managed by AWS CodeBuild**.

* For **Operating System**, choose **Ubuntu**.
* For **Runtime**, choose **Python**.
* For **Version**, choose **aws/codebuild/python:3.6.5**.
* For **Build specification**, choose **Use the buildspec.yml in the source code root directory.**
* Under **AWS CodeBuild service role**,  choose **Create role**. On the IAM console page that describes the role to be created for you, choose **Allow**. On the Step 5: Service Role page, AWS-CodePipeline-Service appears in the drop-down box
* Choose **Save build project**.
* Once build is saved, choose **Next step**.
* On the **Step 4: Deploy** page, from the **Deployment provider** drop-down list, choose **AWS CloudFormation**.
* In **Application name**, type **HQUTriviaApiBackendBuild**.
* Choose **Next step**.
* On the **Step 5: Service Role** page,
* On the **Step 6: Review page**, choose **Create pipeline**.
