from flask import Blueprint, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv
#from schema_extractor import schema_info
from tabulate import tabulate
from rds_schema_extractor import schema_info


load_dotenv()

open_AI_routes = Blueprint('open_AI_routes', __name__)
client = OpenAI(api_key= os.environ['your_api_key'])

def get_response(chat):
    # Create a chat completion with the conversation history
    #Start-time utilizing decorator
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        #model="gpt-4-1106-preview",
        messages=chat
    )#
    #Endtime
    # Return the response text
    return completion.choices[0].message.content

def find_and_save_model_files(base_path):
    model_directories = ['model', 'models', 'entity']
    all_file_contents = []
    allowed_extensions = ('.java', '.class', '.py', '.js')
    counter = 0

    for root, dirs, files in os.walk(base_path):
        if any(model_dir in root for model_dir in model_directories):
            for file in files:
                if file.endswith(allowed_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_contents = file.read()
                            all_file_contents.append({'file_path': file_path, 'content': file_contents})
                            counter+=1
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    print(counter)
    return all_file_contents

def format_schema_info(schema_info):
    formatted_text = "Database Schema:\n"
    for table, details in schema_info.items():
        formatted_text += f"Table: {table}\n"

        # Formatting columns
        columns = details['columns']
        if columns:
            column_headers = ["Column Name", "Type"]
            column_data = [[col['name'], col['type']] for col in columns]
            formatted_text += tabulate(column_data, headers=column_headers, tablefmt="grid")
            formatted_text += "\n\n"

        # Formatting relationships (if any)
        relationships = details['relationships']
        if relationships:
            relationship_headers = ["Column", "References"]
            relationship_data = [
                [rel['column'], f"{rel['references']['table']}({rel['references']['column']})"]
                for rel in relationships
            ]
            formatted_text += tabulate(relationship_data, headers=relationship_headers, tablefmt="grid")
            formatted_text += "\n\n"

        # Get excluded columns for this table
        excluded_columns = details["excluded_columns"]

        # Formatting table data
        table_data = details['data']
        if table_data:
            # Filter out the excluded columns
            filtered_columns = [col for col in details['columns'] if col['name'] not in excluded_columns]

            # Using the filtered column names as headers for the data table
            data_headers = [col['name'] for col in filtered_columns]
            data_rows = [[row[col['name']] for col in filtered_columns] for row in table_data]

            formatted_text += "Table Data:\n"
            formatted_text += tabulate(data_rows, headers=data_headers, tablefmt="grid")
            formatted_text += "\n\n"

    return formatted_text



def handle_initial_schema(base_path):
    model_files = find_and_save_model_files(base_path) #Finds the file contents
    user_input = f"Project model and backend contents:\n{model_files}\n\nThe above lines are the model contents, create a schema from the contents. What questions do you have regarding your schema?"
    
    # This message should be a simple string, not a formatted response
    return [{"role": "user", "content": user_input}]


#modified to include extracting schema_info from schema_extractor.py
@open_AI_routes.route('/ask-openai', methods=['POST'])
def ask_openai():
    try:
        data = request.get_json()

        if 'user_input' not in data:
            return jsonify({'error': 'Missing user_input parameter'}), 400

        user_input = data['user_input']
        chat = data.get('chat', [])

        # Format schema_info into a readable string (implement this function)
        formatted_schema_info = format_schema_info(schema_info)

        # Include schema information in the chat
        schema_message = {"role": "system", "content": formatted_schema_info}
        chat.insert(0, schema_message)  # Insert at the beginning of the chat

        # Add new user message in the correct format
        chat.append({"role": "user", "content": user_input})

        response = get_response(chat)

        # Ensure get_response returns only the assistant's response text
        chat.append({"role": "assistant", "content": response})

        return jsonify({'response': response, 'chat': chat})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
