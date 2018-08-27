import boto3;

def handler(event, context):
  userID = event["queryStringParameters"]["userId"]
  sessionID = event["queryStringParameters"]["sessionId"]
  
  numberCorrect = 9
  numberTotal   = 10
 
  return {
        "statusCode": '200',
        "body": 'Your score on the quiz (user='+str(userId)+',sessionId='+str(sessionId)+') was '+ str(numberCorrect) + ' out of ' + str(numberTotal)
  }
