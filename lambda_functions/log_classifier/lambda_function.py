import json
import boto3

def lambda_handler(event, context):
    comprehend = boto3.client("comprehend")
    log_text = event.get("log", "")
    response = comprehend.detect_sentiment(Text=log_text, LanguageCode="en")
    sentiment = response["Sentiment"]

    # Store classification in DynamoDB (mocked)
    print(f"Classified log as: {sentiment}")
    return {"sentiment": sentiment}