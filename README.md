# AI-Powered Text Narration with Amazon Polly for Natural Speech Synthesis

"AI Voice Generator"

# Technical Architecture

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/c0ffc610d4e7e96203fcc7cd694102494e4e1470/img/Screenshot%202025-01-31%20084804.png)

## Project Overview

We are going to create a serverless text-to-speech (TTS) system using AWS services. A client submits text via an API Gateway, which triggers an AWS Lambda function. The function sends the text to Amazon Polly, which converts it into speech and returns an MP3 file. Lambda then stores the audio file in an S3 Bucket for retrieval and use. This architecture enables scalable and cost-efficient TTS applications for accessibility, voice notifications, and automated content creation.

## Project Objectives

1.Amazon S3: Store generated MP3 files in an S3 bucket for easy access and playback.

2.Amazon Polly: Convert user-submitted text into high-quality speech.

3.AWS Lambda:  to handle text processing without managing servers..

4.API Gateway: Provide a seamless API for users to interact with the service programmatically.

## Prerequisites

1.AWS Account: Create an AWS Account

2.AWS CLI Installed and Configured: Install & configure AWS CLI to programatically interact with AWS

## Technologies

1.Amazon S3

2.AWS Lambda

3.Amazon Polly

4.API Gateway

5.Postman


## Step 1: Configure Amazon S3 Bucket


1.1.Login to AWS Console:

Access the AWS Management Console and search for Amazon S3.

1.2.Create a bucket and give it name that is globally unique 

Choose create bucket and leave everything as default

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/296ff2fb3aa29813700a52b69cca9a9e6bfb82d0/img/Screenshot%202025-01-31%20100742.png)


1.3.Now that our bucket is successfully created see example, leave the bucket empty becuase lambda will save the mp3 audios here.

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/deecbbb3d811482ade41b04d4d173a420b674353/img/Screenshot%202025-01-31%20100804.png)


##  Step 2: Configure IAM Role for AWS Lambda

2.1.Navigate to "IAM" home console search Roles on your left hand side click on it and you will see a orange button that says create role


2.2.AWS Services: select Lambda

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/0137cd19b32e65ca70f977d708690421ba1b9aa8/img/Screenshot%202025-01-31%20100852.png)


2.3.On Policies we are to choose three policies

Attach the following policies:

Amazon S3:`AmazonS3FullAccess `

Amazon API Gateway:`AmazonAPIGatewayInvokeFullAccess `

Amazon Polly:`AmazonPollyFullAccess `


2.4.Give your Role a name see example- then click create Role

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/8f35f4212e8378def4e6fab6d7e4b08b7e2d353a/img/Screenshot%202025-01-31%20101111.png)


## Step 3: Configure a AWS Lambda function 

3.1.Search for Lambda click on the orange buttun to create a function see example below-

3.2.Choose Start Author from Scratch and give your lambda function a name


![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/870387452468c32c4e0a2223db1f84cbbb982387/img/Screenshot%202025-01-31%20101314.png)


3.3.Now add Permissions choose the existing role that we have created ealier see example below-

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/fdc1003b56f10abffd57860c9b19d952deec0163/img/Screenshot%202025-01-31%20101335.png)


Proceed to create your functin by clicking the orange button below

3.4.Now that our lambda function was successfully created copy the code below and paste it on the lambda code block and click deploy.


```python
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



```


## code explanation

This AWS Lambda function converts text into speech using Amazon Polly and stores the resulting audio file in an S3 bucket. When triggered by an API Gateway event, it extracts the text from the request body and initializes Polly and S3 clients. 

Polly generates speech from the text using the specified voice (e.g., "Matthew"), and the resulting MP3 file is given a unique filename using `uuid`. The audio file is then uploaded to an S3 bucket `(text-narrator-audio)`. Finally, the function returns the public URL of the stored MP3 file, allowing users to access the generated speech audio.


## Step 4: Configure a API Gateway

4.1.Search for API Gateway click on the orange buttun to create a function see example below-

Click "Create API."

Choose "HTTP API" and click "Build."

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/8d94db51e986d7428b742d03a4a9840841e7ef7f/img/Screenshot%202025-01-31%20101628.png)


4.2.Name the API with any name you want


![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/0c76d92477a6229f76bb034fa633a0d3cda74e66/img/Screenshot%202025-01-31%20101708.png)


Click "Next."


4.3.Add a Resource 

Under Resources "click" create Resource and name it "narrater"

Note: Enable the CORS feature

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/90f970867529613ca009bbbe4c731a68c1ef0e95/img/Screenshot%202025-01-31%20101835.png)


4.4.Set the method to `POST` and the path to `/narrate`.

Under "Attach integrations," select "Lambda."

Choose the Lambda function you created earlier 

Click "Next."


![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/eb1396b35165f845d13424575e50c507aab40c59/img/Screenshot%202025-01-31%20101946.png)


Review the settings and click "Create."

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/d1be90620592badb4a5c63b32681a721a16cb49a/img/Screenshot%202025-01-31%20102132.png)


4.5.Deploy the API:

Click "Deploy API."

Choose a stage (e.g., `prod`).

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/cb1eb6866fd7a2931e94f7f7999d10c874b382f3/img/Screenshot%202025-01-31%20102150.png)


Note the API endpoint URL (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod`).

![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/392b238a87721c385d67f040ca8de7f1eeb0037c/img/Screenshot%202025-01-31%20102214.png)


## Step 5: Test the API

5.1.Use a tool like Postman to send a POST request to the API endpoint:

URL: `https://<api-id>.execute-api.<region>.amazonaws.com/prod/narrate`

Method: `POST`

Body: `{"body": "Hello, this is a test narration."}`


![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/515d21127ab197bc883f791672dbdefbaf1224cf/img/Screenshot%202025-01-31%20103921.png)


5.2.The response will contain the S3 URL of the generated audio file.


## Step 6: Verify the Audio File in S3


6.1.Go to the S3 Console.


6.2.Navigate to your bucket (text-narrator-audio).


6.3.Verify that the audio file is present and downloadable.


![image_alt](https://github.com/Tatenda-Prince/Creating-Text-Narrator-Using-Amazon-Polly/blob/816fe73e32d61d159b635c6116485adecab61ed0/img/Screenshot%202025-01-31%20103952.png)



# Congratulations

We have Successfully created Amazon Polly which converts text into lifelike speech, enabling applications to interact with users in a more natural way. AWS Lambda handles the logic by processing incoming requests, interacting with Amazon Polly to generate speech, and storing the resulting audio files in Amazon S3. API Gateway acts as the front-facing interface, exposing the Lambda function as an HTTP endpoint, allowing users or applications to send text input and receive the corresponding speech output. Amazon S3 serves as the storage solution, securely holding the generated audio files for retrieval or further processing.










































