from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import json
import bcrypt

app = FastAPI()

@app.get("/userpage", response_class=HTMLResponse)
def userpage(username):
    return HTMLResponse(f"""
        <html>
            <body>
                <h1>CONGRATULATIONS, {username}!</h1>
                <p>You have successfully signed in.</p>
            </body>
        </html>
    """)


@app.get("/wronglogin", response_class=HTMLResponse)
def wronglogin():
    return HTMLResponse("""
        <html>
            <body>
                <h1>Login Failed</h1>
                <p>Incorrect username or password.</p>
                <a href="/">
                    <button>Try Again</button>
                </a>
            </body>
        </html>
    """)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>WELCOME TO BRANCOIN</h1>
            <h2>Sign In</h2>
            <form action="/signin" method="post">
            
                    <input name="username" type="text" placeholder="Username">
                    <input name="password" type="password" placeholder="Password">
                    <button type="submit">Submit</button>

           </form>         
            <a href="/create">
                <button>Create New Account</button>
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

@app.post("/signin")
def signin(username: str = Form(...), password: str = Form(...)):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    for i in users:
        if i["username"] == username:
            if bcrypt.checkpw(password.encode(), i["password"].encode()):
                return userpage(username)
    return wronglogin()

@app.post("/create")
def save_account(username: str = Form(...), password: str = Form(...)):

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    for i in users:
        if i["username"] == username:
            return {"message":"User Name already taken"} 

    salt = bcrypt.gensalt()
    pw = bcrypt.hashpw(password.encode(), salt).decode()

    #add to db
    users.append({
        "username": username,
        "password": pw
    })

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    return userpage(username)

