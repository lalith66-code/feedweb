from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = "feedback.xlsx"

if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Role", "Parent Name", "Child Name", "Child Class",
                               "Student Name", "Student Class", "Student Orientation",
                               "Teacher Name", "Rating", "Comment"])
    df.to_excel(EXCEL_FILE, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form.get("role")
        parent_name = request.form.get("parent_name", "")
        child_name = request.form.get("child_name", "")
        child_class = request.form.get("child_class", "")
        student_name = request.form.get("student_name", "")
        student_class = request.form.get("student_class", "")
        student_orientation = request.form.get("student_orientation", "")
        teacher_name = request.form.get("teacher_name", "")
        rating = request.form.get("rating", "")
        comment = request.form.get("comment", "")

        df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([df, pd.DataFrame([{
    "Role": role,
    "Parent Name": parent_name,
    "Child Name": child_name,
    "Child Class": child_class,
    "Student Name": student_name,
    "Student Class": student_class,
    "Student Orientation": student_orientation,
    "Teacher Name": teacher_name,
    "Rating": rating,
    "Comment": comment
}])], ignore_index=True)

        df.to_excel(EXCEL_FILE, index=False)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

