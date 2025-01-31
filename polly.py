import boto3
import os
import uuid

def lambda_handler(event, context):
    # Extract text from the API Gateway event
    text = event['body']
    
    # Initialize Polly and S3 clients
    polly = boto3.client('polly')
    s3 = boto3.client('s3')
    
    # Generate a unique filename
    filename = f"{uuid.uuid4()}.mp3"
    
    # Synthesize speech using Polly
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Matthew"  # You can change the voice (e.g., "Matthew", "Salli")
    )
    
    # Save the audio file to S3
    s3.put_object(
        Bucket="text-narrator-audio",  # Replace with your S3 bucket name
        Key=filename,
        Body=response['AudioStream'].read()
    )
    
    # Return the S3 file URL
    return {
        'statusCode': 200,
        'body': f"https://text-narrator-audio.s3.amazonaws.com/{filename}"
    }