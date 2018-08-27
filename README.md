# hqu-trivia-api-backend
This is the set of lambda functions that will be used by the DialogFlow agent in the HQU Trivia application for Google Assistant. 


* Sign in to the AWS Management Console and open the AWS CodePipeline console at http://console.aws.amazon.com/codepipeline.
* On the Welcome page, choose **Create pipeline**.

If this is your first time using AWS CodePipeline, choose **Get Started Now**.
* On the **Step 1: Name page**, in Pipeline name, type **HQUTriviaApiBackend**, and then choose **Next step**.

* On the **Step 2: Source page**, in the Source provider drop-down list, choose **Github**, and then choose **Next step**.

* Choose the GitHub repository **thebrigade/hqu-trivia-api-backend** yas the source location for your pipeline. In Branch, from the drop-down list, choose the **master** branch.

* On the **Step 3: Build page**,  choose **AWS CodeBuild**.
* Choose **Create a new build project**.
* Choose **Use the buildspec.yml in the source code root directory.**
* Choose **Next step**.
* From the **Deployment provider** drop-down list, choose **AWS CodeDeploy**.
* In **Application name**, type **HQUTriviaApiBackendBuild**.
* Choose **Next step**.
* On the **Step 5: Service Role** page, choose **Create role**. On the IAM console page that describes the role to be created for you, choose **Allow**. On the Step 5: Service Role page, AWS-CodePipeline-Service appears in the drop-down box
* On the **Step 6: Review page**, choose **Create pipeline**.
