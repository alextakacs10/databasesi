from flask import Flask, render_template, url_for, redirect
import database
import queries
import psycopg2


app = Flask(__name__)


@app.route("/")
def main_menu():
    """This function is the vessel of the menu options and the corresponding
       URLs. Returns these pairs so they can be used in the index.html page.
    """
    title = "Main menu"
    page_url_pairs = (("Mentors and school", "mentors"),
                      ("All school", "all-school"),
                      ("Mentors by country", "mentors-by-country"),
                      ("Contacts", "contacts"),
                      ("Applicants", "applicants"),
                      ("Applicants and mentors", "applicants-and-mentors"))

    return render_template("index.html", main_menu=page_url_pairs, title=title)


@app.route("/mentors/")
def show_mentors_and_schools():
    title = "Mentors and school"
    headers, mentors_and_schools = queries.get_mentors_and_schools()

    return render_template('results.html', colnames=headers, data=mentors_and_schools)


@app.route("/all-school/")
def get_mentors_and_all_schools():
    title = "All school"
    headers, mentors_and_all_schools = queries.get_mentors_and_all_schools()

    return render_template('results.html', colnames=headers, data=mentors_and_all_schools)


@app.route("/mentors-by-country/")
def get_mentors_by_country():
    title = "Mentors by country"
    headers, mentors_by_country = queries.get_mentors_by_country()

    return render_template('results.html', colnames=headers, data=mentors_by_country)


@app.route("/contacts/")
def get_contacts():
    title = "Contacts"
    headers, contacts = queries.get_contacts()

    return render_template('results.html', colnames=headers, data=contacts)


@app.route("/applicants/")
def get_applicants_by_creation():
    title = "Applicants"
    headers, applicants_by_creation = queries.get_applicants_by_creation()

    return render_template('results.html', colnames=headers, data=applicants_by_creation)


@app.route("/applicants-and-mentors/")
def get_applicants_and_mentors():
    title = "Applicants and mentors"
    headers, applicants_and_mentors = queries.get_applicants_and_mentors()

    return render_template('results.html', colnames=headers, data=applicants_and_mentors)


if __name__ == '__main__':
    app.run(debug=True, port=2017)