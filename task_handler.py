import psycopg2
import sys

try:
    # setup connection string
    connect_str = "dbname='alextakacs10' user='alextakacs10' host='localhost' password='ohhithere'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def show_every_mentor():
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    mentors = list(cursor.fetchall())
    for num, data in enumerate(mentors):
        print("{}. mentor: {} {}".format(num, data[0], data[1]))


def get_mentor_nicknames_by_city(city):
    cursor.execute("""SELECT first_name, last_name, nick_name FROM mentors WHERE city = '{}';""".format(city))
    mentors = list(cursor.fetchall())
    for data in mentors:
        print("{} {}'s nickname is: {}".format(data[0],data[1], data[2]))


def get_phone_number_by_first_name(first_name):
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                      FROM applicants WHERE first_name = '{}'""".format(first_name))
    applicant_info = cursor.fetchall()
    print("{}'s phone number is {}".format(applicant_info[0][0], applicant_info[0][1]))


def get_phone_number_by_email(email):
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                        FROM applicants WHERE email LIKE '%{}'""".format(email))
    applicant_info = cursor.fetchall()
    print("{}'s phone number is {}".format(applicant_info[0][0], applicant_info[0][1]))


def insert_new_applicant(first_name, last_name, phone_number, email, application_code):
    cursor.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                      VALUES ('{}', '{}', '{}', '{}', {});""".format(first_name, last_name, phone_number, email, application_code))


def show_applicant_info(application_code):
    cursor.execute("""SELECT * FROM applicants WHERE application_code = {}""".format(application_code))
    applicant = cursor.fetchall()
    print("Our new applicant is {} {}, phone number: {}, email address: {} with {} as application id.".format(applicant[0][1],
                                                                                                              applicant[0][2],
                                                                                                              applicant[0][3],
                                                                                                              applicant[0][4],
                                                                                                              applicant[0][5]))


def change_phone_number(phone_number, first_name, last_name):
    cursor.execute("""UPDATE applicants
                      SET phone_number = '{}'
                      WHERE first_name = '{}' AND last_name = '{}';
                      SELECT first_name, last_name, phone_number FROM applicants
                      WHERE first_name = '{}' AND last_name = '{}';""".format(phone_number, first_name, last_name, first_name, last_name))
    applicant = cursor.fetchall()
    print("{} {}'s phone number was updated to {}.".format(applicant[0][0], applicant[0][1], applicant[0][2]))


def delete_by_email(email):
    cursor.execute("""DELETE FROM applicants
                      WHERE email LIKE '%{}'""".format(email))
    applicant = cursor.fetchall()
    print("Everybody with the email address ending in {} was deleted from the database.".format(email))

if __name__ == '__main__':
    main()
