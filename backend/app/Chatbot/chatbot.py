import os
from openai import OpenAI

# Instantiate the client with your API key
client = OpenAI(api_key= "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")

def get_response(messages):
    # Create a chat completion with the conversation history
    #Start-time utilizing decorator
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    #Endtime
    # Return the response text
    return completion.choices[0].message.content

def handle_initial_schema():
    messages = [] # Memory for the conversation
    user_input = """Schema:
                HR.JOBS
                Column_Name Null? Type
                JOB_ID NOT NULL VARCHAR2(10)
                JOB_TITLE NOT NULL VARCHAR2(35)
                MIN_SALARY NUMBER(6)
                MAX_SALARY NUMBER(6)

                HR.EMPLOYEES
                Column_Name Null? Type
                EMPLOYEE_ID NOT NULL NUMBER(6)
                FIRST_NAME VARCHAR2(20)
                LAST_NAME NOT NULL VARCHAR2(25)
                EMAIL NOT NULL VARCHAR2(20)
                PHONE_NUMBER VARCHAR2(20)
                HIRE_DATE NOT NULL DATE
                JOB_ID NOT NULL VARCHAR2(10)
                SALARY NUMBER(8,2)
                COMMISSION_PCT NUMBER(2,2)
                MANAGER_ID NUMBER(6)
                DEPARTMENT_ID NUMBER(4)
                
                HR.JOB_HISTORY
                Column_Name Null? Type
                EMPLOYEE_ID NOT NULL NUMBER(6)
                START_DATE NOT NULL DATE
                END_DATE NOT NULL DATE
                JOB_ID NOT NULL VARCHAR2(10)
                DEPARTMENT_ID NUMBER(4)

                The above lines are the schema, the user will now ask questions regarding it. You will now ask, "What questions do you have regarding your schema?".
                """
    messages.append({"role": "user", "content": user_input})
    response = get_response(messages)
    messages.append({"role": "assistant", "content": response})
    print("AI:", response)
    return messages

def main():
    messages = handle_initial_schema()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input + "(Please make sure to only answer questions relevant to schemas.)"})
        response = get_response(messages)
        messages.append({"role": "assistant", "content": response})
        print("AI:", response)

if __name__ == "__main__":
    main()