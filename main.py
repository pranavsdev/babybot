import socket
import sys

from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from resources import index_html_response, enter_details, hello_html_response, login_details, chatbot_ques_html, chatbot_ans_html

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
hostname = socket.gethostname()

@app.get("/")
async def read_root():
    return {
        "name": "babybot",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python"
    }

@app.get("/hello/", response_class=HTMLResponse)
async def hello():
    return hello_html_response()

@app.get("/index/", response_class=HTMLResponse)
async def read_items():
    return index_html_response()

@app.get("/login/", response_class=HTMLResponse)
async def details():
    return enter_details()

@app.get("/chatbot_question/", response_class=HTMLResponse)
async def chatbot_ques():
    return chatbot_ques_html()

@app.post("/chatbot_answer/", response_class=HTMLResponse)
async def chatbot_ans(request: Request, question: str = Form(...)):
    return chatbot_ans_html(question)

@app.post("/check_login/",response_class=HTMLResponse)
async def check_details(request: Request, username: str = Form(...), password: str = Form(...)):
    print(username)
    print(password)
    #return login_details(request)

@app.post("/form")
def form_post(request: Request, username: str = Form(...)):
    result = username
    print(username)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})