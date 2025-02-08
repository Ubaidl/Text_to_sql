import os
import sqlite3
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
import streamlit as st

#mykey="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"
mykey= os.getenv("GROQ_API_KEY")

#create an instance of the Groq client with the API key
client = Groq(api_key="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")


# create a function to load groq model and provide query as response

def load_groq_model( question ,prompt):
    # Pass the prompt and question dynamically
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},  # The prompt is passed as an argument
            {"role": "user", "content": question}  # The question is passed as an argument
        ],
        model="llama-3.3-70b-versatile"
    )
    
    # You can return or process the response as needed
    response=chat_completion.choices[0].message.content
    return response


# function to retrieve the query from the sql database .in simple  , ths function if ofr it will take the sql query and hit the data base and get the result
def get_result_from_databast(sql,db):
    connection=sqlite3.Connection(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    
    return rows




prompt="""
you are an expert in converting english question into sql query! the sql database 
has the  name STUDENT and has the folowing colimns ,name class section marks
for example  how many entries of records are present? the sql command will be  like
SELECT COUNT(*) from STUDENT
exampl2: tell me all students studying in ml  ? the sql command wille be  SELECT * from Student wher class="ml 

also the sql query code should not have ''' in begning aor end and sql word:


"""
st.header("Groq app to reqrieve sql data")
question= st.text_input("ASk  a question")
submit= st.button("sumbit")
if submit:
    response= load_groq_model(question,prompt)
    # print(response)

    data=get_result_from_databast(response,"STUDENT.db")
    for row in data:
        st.header(row)
    









 











 # for checking
# question="who is the prime minister of india"
# prompt='you are  AI assistenat  give the answer what ever user ask'
# ans=load_groq_model(prompt,question)
# print(ans)







