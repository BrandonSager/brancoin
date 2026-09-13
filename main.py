from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>WELCOME TO BRANCOIN</h1>

            <a href="/create">
                <button>Create Account</button>
            </a>
        </body>
    </html>
    """

@app.get("/create", response_class=HTMLResponse)
def create():
    return """
    <html>
        <body>
            <h1>Create Account</h1>

            <form action="/create" method="post">

                <input name="username" type="text" placeholder="Username">
                <input name="password" type="password" placeholder="Password">
                <button type="submit">Submit</button>

            </form>
        </body>
    </html>
    """

@app.post("/create")
def save_account(username: str = Form(...), password: str = Form(...)):

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    with open("users.json", "r") as file:
        users = json.load(file)

    for i in users:
        if i["username"] == username:
            return {"message":"User Name already taken"} 

    users.append({
        "username": username,
        "password": password
    })

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    return {"message": "Account created!"}