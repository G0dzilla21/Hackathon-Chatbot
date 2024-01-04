# Project Setup Instructions

This guide walks you through setting up the project on your local machine.

## Getting Started

### Setting Up the Backend

1. **Open a Terminal Window.**
2. **Navigate to the Backend Directory:**
   ```bash
   cd backend
Install the Required Python Packages:
bash
Copy code
pip install -r requirements.txt
Start the Flask Application:
bash
Copy code
flask run
Setting Up the Frontend
Open Another Terminal Window.
Navigate to the Frontend Directory:
bash
Copy code
cd frontend
Install Node.js Dependencies:
bash
Copy code
npm install
Start the Frontend Application:
bash
Copy code
npm start
Configuration
Creating the .env File
Create a .env file in the main project directory (where the frontend and backend folders are located) and add the following contents:

env
Copy code
SECRET_KEY=<your_secret_key>
DATABASE_URL=mysql+pymysql://root:<password>@localhost/sakila
SCHEMA=<your_schema_name>
your_api_key=<your_openai_api_key>
Replace the placeholders (<your_secret_key>, <password>, <your_schema_name>, <your_openai_api_key>) with your actual values.

Note: The DATABASE_URL is just an example. Replace root, <password>, and sakila with your actual MySQL username, password, and database name.

Important Notes
Ensure that you have Python and Node.js installed on your system before starting.
The API keys and secret keys should be kept confidential and not shared publicly.
