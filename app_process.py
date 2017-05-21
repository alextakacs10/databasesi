import psycopg2
from file_handler import import_sql
import sys
import task_handler

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


def reset(filename):
    '''Resets database with data from sample file
    '''
    try:
        commands = import_sql(filename)
        cursor.execute(commands)
        print("You have successfully reset the database!")
    except:
        print("Database reset failed.")
        sys.exit()


def get_user_status():
    status = input("Are you working right now? [y/n]")  
    if status == "y":
        at_work = True
    else:
        at_work = False
    return at_work


def show_menu():
    print("\nWelcome! The HR department wants you to do the following tasks today: \n")
    tasks = ["Get the first name and the last name of all the mentors",
             "Get the nickname of every mentor working at Miskolc",
             "Get the full name and phone number of Carol, who may have left her hat at us.",
             "If it wasn't Carol, there might be another girl. Pleace get her full name and phone number, all they know is her email address is ending in @adipiscingenimmi.edu.",
             "A new applicant appeared. Please add him to the database with the following info: Markus Schaffarzyk, 003620/725-2666, djnovus@groovecoverage.com, 54823. After that, please print his info.",
             "Jemima Foreman changed her phone number to 003670/223-7459, please update it in the database.",
             "Arsenio and his friend from mauriseu.net canceled the application process. Please delete them from our database. You can find them by their email address ending in @mauriseu.net."]
    for num, task in enumerate(tasks):
        print("{}. {}".format(num+1, task))
    print("\nIf you are done, you can go home. Just press [q] to quit.")
    print("To reset the database with sample data press [r].")
    print("\n----------------------------")


def back_to_main_menu():
    answer = input("\nWould you like to jump back to the main menu? [y/n]")
    try:
        if answer == "y":
            show_menu()
        else:
            sys.exit()
    except:
        print("\nAction unknown.")
        back_to_main_menu()


def main():
    at_work = get_user_status()
    if not at_work:
        print("Okay, good bye then!")

    while at_work:
        show_menu()
        action = input("What would you like to do? ")

        if action == "r":
            reset("application_process_sample_data.sql")

        elif action == "q":
            sys.exit("Goodbye!")

        elif action == "1":
            task_handler.show_every_mentor()
            back_to_main_menu()

        elif action == "2":
            task_handler.get_mentor_nicknames_by_city("Miskolc")
            back_to_main_menu()

        elif action == "3":
            task_handler.get_phone_number_by_first_name("Carol")
            back_to_main_menu()

        elif action == "4":
            task_handler.get_phone_number_by_email("@adipiscingenimmi.edu")
            back_to_main_menu()

        elif action == "5":
            try:
                task_handler.insert_new_applicant("Markus", "Schaffarzyk", "003620/725-2666", "djnovus@groovecoverage.com", 54823)
            except:
                print("User with this application ID already exists.")
                back_to_main_menu()
            task_handler.show_applicant_info(54823)
            back_to_main_menu()

        elif action == "6":
            task_handler.change_phone_number("003670/223-7459", "Jemima", "Foreman")
            back_to_main_menu()

        elif action == "7":
            try:
                task_handler.delete_by_email("mauriseu.net")
            except:
                print("No user(s) with such email address to delete.")
            back_to_main_menu()
        else:
            print("Sorry, action or task does not exist.")


if __name__ == '__main__':
    main()