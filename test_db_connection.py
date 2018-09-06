import boto3;
import mysql.connector;
import config;

def handler(event, context):
    all_labels = ['alpha','beta','gamma','delta]
    csv_labels = ", ".join(all_labels)
    print("Detect_labels finished. Key: [%s], Labels: [%s]" % (key, csv_labels))

    conn = mysql.connector.connect(user=config.DATABASE_USER, password=config.DATABASE_PASSWORD,
                                   host=config.DATABASE_HOST,
                                   database=config.DATABASE_DB_NAME)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT object_key, description, labels, created_datetime
                      FROM photo""", (key,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    #return True
    return {
        "statusCode": '200',
        "body": 'It works--connected'
    }
