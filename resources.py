from fastapi.responses import HTMLResponse
import urllib
from bs4 import BeautifulSoup
from fastapi import Request as request
from fastapi import FastAPI, Form
from starlette.requests import Request
from collections import defaultdict

def index_html_response():
    html_content = """
        <html>
            <body>
                <button onclick="window.location.href='/index'">Home</button>
                <button onclick="window.location.href='/hello'">Hello</button><br><br><br>
                <button onclick="window.location.href='/chatbot_question'">Chatbot</button><br><br><br>
                <button onclick="window.location.href='/login'">Details</button><br><br><br>

            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def hello_html_response():
    html_content = """
        <html>
            <body>
                <button onclick="window.location.href='/index'">Home</button><br>
                <b>hello world!</b>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def enter_details():
    html_content="""<form action=/check_login method='POST'> 
                    <label> Username </label> 
                    <input type='text' name='username'> 
                    <label> Password </label> 
                    <input type='text' name='password'> 
                
                    <button type='submit'> Submit </button> 
                    </form> """
 
    soup = BeautifulSoup(html_content)
    print(soup.get_text())
    #print("html content",html_content)
    return HTMLResponse(content=html_content, status_code=200)

def chatbot_ques_html():
    html_content="""<form action=/chatbot_answer method='POST'> 
                    <br><br><br><br><br><br>
                    <label> Ask me anything </label> <br><br>
                    <input type='text' name='question' maxlength="30" size="50"> 
                
                    <button type='submit'> Submit </button> 
                    </form> """

    return HTMLResponse(content=html_content, status_code=200)

def chatbot_ans_html(question):
    with open("chatbot_sample_intents.csv", "r") as f:
        content = f.readlines()

    text_fields = question.split(" ")
    predict_answer = {}
    for line in content:
        fields = line.strip().split(",")
        target = fields[0]
        count = sum([1 for word in text_fields if word in fields[1:]])
        predict_answer[target] = count

    answer = max(predict_answer, key=predict_answer.get)

    html_content="""<html>
            <body>
            <br><br><br><br><br><br>
            """ + answer + """
            <br><br><button onclick="window.location.href='/chatbot_question'">Another question</button>
            <button onclick="window.location.href='/index'">Home</button>

            </body>
        </html> """

    return HTMLResponse(content=html_content, status_code=200)

def login_details(request):

    print("request is--->",Request.stream('username'))
    #username=request.form['username']
    #password = request.form['password']
    #print("username is--->",username)
    #print(password)
    #return username, password