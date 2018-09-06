import boto3;
import mysql.connector;
import config;
import string;
import random;

def handler(event, context):
    all_labels = ['cow','animal','beautiful']
    csv_labels = ", ".join(all_labels)
    key        = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    description = "a mighty cow"
    
    print("Attempting database connection...")
    
    conn = mysql.connector.connect(user=config.DATABASE_USER, password=config.DATABASE_PASSWORD,
                                   host=config.DATABASE_HOST,
                                   database=config.DATABASE_DB_NAME)
    
    
    conn.cursor().execute("INSERT INTO photo (object_key, description, labels, created_datetime) VALUES (%s,%s,%s,now())",
                              (key,description,csv_labels))
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT object_key, description, labels, created_datetime
                      FROM photo""")
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    #return True
    return {
        "statusCode": '200',
        "body": 'It works--connected'
    }
