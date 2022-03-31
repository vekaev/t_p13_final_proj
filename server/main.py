from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse
from os.path import join, dirname, exists
import sqlite3

app = FastAPI()

FILE_PATH = join(dirname(__file__), 'client_forms.txt')

DB_URL = 'clients.sqlite'

connection = sqlite3.connect(DB_URL, check_same_thread=False)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS [clients](
	id INTEGER PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone VARCHAR(255)
);
''')

def save_user(*user):
    cursor.execute(f'INSERT INTO [clients] (name, email, phone) VALUES(?,?,?)', user)
    connection.commit()
    # with open(FILE_PATH, 'a') as f:
    #     f.write(str(user) + '\n')

def get_all_users():
    cursor.execute('SELECT * FROM [clients]')
    return cursor.fetchall()
    # users = []
    # if exists(FILE_PATH):
    #     with open(FILE_PATH) as f:
    #         for line in f:
    #             users.append(eval(line.rstrip()))
    # return users

# users = []

@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Backend for Portfolio</title>
        </head>
        <body>
            This is Backend for Portfolio website <a href="https://vekaev.github.io/t_p13_final_proj">https://vekaev.github.io/t_p13_final_proj/</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get('/client_form')
def save_data(name, email, phone=None):
    user = {
        "name": name,
        "email": email,
        "phone": None
    }

    if not phone or (phone and len(phone) > 6):
        user["phone"] = phone
    else:
        raise HTTPException(status_code=422, detail="Incorrect phone number")

    save_user(user)

    return user


@app.get('/all_client_form')
def all_client_form():
    users = get_all_users()
    return users
