from flask import Flask, request

app = Flask(__name__)

students = ["Vasif", "Anu", "Ravi"]


@app.get("/")
def home_page():
    return "Hello student"


@app.get("/students")
def students_page():
    return {"response": students}


@app.post("/students/register")
def students_register():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return {"response": "The key not found", "status": 400}, 400

    students.append(name)
    print(data)
    return {"response": name, "status": 201}, 201


app.run(use_reloader=True)