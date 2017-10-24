"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_details = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_details=project_details)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student")
def add_student():
    """Add a student."""

    html = render_template("add_student.html")

    return html


@app.route("/display-student", methods=['POST'])
def display_student():
    """Add new student to database."""

    first_name = request.form.get('first')
    last_name = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("new_student.html", github=github)


@app.route("/project")
def show_project_info():
    """Show project information"""

    title = request.args.get('title')
    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)

    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
