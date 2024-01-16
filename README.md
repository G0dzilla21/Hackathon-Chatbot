# Project Setup Instructions

This guide walks you through setting up the project on your local machine.

## Getting Started

### Setting Up the Backend

1. **Open a Terminal In IDE**.
2. **Navigate to the Backend Directory:**
   ```
   cd backend
   ```
3. **Install the Required Python Packages:**
   ```
   pip install -r requirements.txt
   ```
4. **Start the Flask Application:**
   ```
   flask run
   ```

## Configuration

### Creating the .env File

Create a `.env` file in the main project directory (where the frontend and backend folders are located) and add the following contents:

```
SECRET_KEY=<your_secret_key>
DATABASE_URL=mysql+pymysql://root:<password>@localhost/sakila
SCHEMA=<your_schema_name>
your_api_key=<your_openai_api_key>
```

Replace the placeholders (`<your_secret_key>`, `<password>`, `<your_schema_name>`, `<your_openai_api_key>`) with your actual values.

**Note:** The `DATABASE_URL` is just an example. Replace `root`, `<password>`, and `sakila` with your actual MySQL username, password, and database name.


### Setting Up the Frontend

1. **Open Another Terminal IDE**.
2. **Navigate to the Frontend Directory:**
   ```
   cd frontend
   ```
3. **Install Node.js Dependencies:**
   ```
   npm install
   ```
4. **Start the Frontend Application:**
   ```
   npm start
   ```

## Important Notes

- Ensure that you have Python and Node.js installed on your system before starting.
- The API keys and secret keys should be kept confidential and not shared publicly.
