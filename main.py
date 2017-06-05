from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
def main_menu():
    """This function is the vessel of the menu options and the corresponding
       URLs. Returns these pairs so they can be used in the index.html page.
    """
    title = "Main menu"
    page_url_pairs = (("Mentors and school page", "mentors"),
                      ("All school page", "all-school"),
                      ("Contacts page-m", "mentors-by-country"),
                      ("Contacts page-s", "contacts"),
                      ("Applicants page", "applicants"),
                      ("Applicants and mentors page", "applicants-and-mentors"))

    return render_template("index.html", main_menu=page_url_pairs, title=title)


if __name__ == '__main__':
    app.run(debug=True, port=2017)