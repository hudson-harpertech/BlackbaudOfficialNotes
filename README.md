# Blackbaud SIS to BigQuery Sync

This repository contains a Python application designed to sync official notes from Blackbaud's Student Information System (SIS) to Google BigQuery using the Blackbaud SKY API.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a Blackbaud account with access to the SKY API.
- You have a Google Cloud account and a BigQuery dataset.
- You have Python 3.8+ installed on your local machine.

## Local Setup

1. **Clone the Repository**:
   ```sh
   git clone [REPO_URL]
   cd [REPO_NAME]
   ```
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
Create a .env file with the following variables:

* BB_API_KEY: Your Blackbaud API key.
* CLIENT_ID: Your Blackbaud client ID.
* CLIENT_SECRET: Your Blackbaud client secret.
* REDIRECT_URI: Your OAuth2 redirect URI.

4. **Generate Refresh Token**:
Run the code locally to authorize your application and generate a refresh token. The token will be saved in .sky-token.

## Deployment to Google Cloud
1. **Google Cloud SDK**:
Ensure the Google Cloud SDK is installed and configured on your local machine.

2. **Build Docker Image**:
  ```sh
  gcloud builds submit --tag gcr.io/[PROJECT-ID]/[IMAGE-NAME]
  ```
3. **Push to Artifact Registry**:
Make sure you have created an Artifact Registry repository in Google Cloud.
   ```sh
   gcloud auth configure-docker
   docker push gcr.io/[PROJECT-ID]/[IMAGE-NAME]
   ```
4. **Deploy to Cloud Run**:
   ```sh
   gcloud run deploy --image gcr.io/[PROJECT-ID]/[IMAGE-NAME] --platform managed
   ```

## Usage
1. **Configuring Advanced List Number**:
The advanced list number in main.py should be updated to match your specific Blackbaud environment.

2. **Running the Application**:
Once deployed, the application will automatically sync official notes from Blackbaud SIS to your BigQuery table.

3. **Support**
For support, contact hudson.harper@downtownschoolseattle.org or raise an issue in the repository.

Please replace `[REPO_URL]`, `[REPO_NAME]`, `[PROJECT-ID]`, `[IMAGE-NAME]`, and `[YOUR EMAIL]` with the appropriate details for your project.
