# Creating-Text-Narrator-Using-Amazon-Polly

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

![image_alt]()


1.3.Now that our bucket is successfully created see example, leave the bucket empty becuase lambda will save the mp3 audios here.

![image_alt]()


##  Step 2: Configure IAM Role for AWS Lambda

2.1.Navigate to "IAM" home console search Roles on your left hand side click on it and you will see a orange button that says create role


2.2.AWS Services: select Lambda

![image_alt]()


2.3.On Policies we are to choose three policies

Attach the following policies:

Amazon S3:`AmazonS3FullAccess `

Amazon API Gateway:`AmazonAPIGatewayInvokeFullAccess `

Amazon Polly:`AmazonPollyFullAccess `


2.4.Give your Role a name see example- then click create Role

![image_alt]()








