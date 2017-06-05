import database


def get_mentors_and_schools():
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors
               JOIN schools ON mentors.city = schools.city
               ORDER BY mentors.id;"""
    result = database.handle_data(query)
    return result


def get_mentors_and_all_schools():
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors
               RIGHT JOIN schools ON mentors.city = schools.city
               ORDER BY mentors.id;"""
    result = database.handle_data(query)
    return result


def get_mentors_by_country():
    query = """SELECT schools.country, COUNT(mentors.id) AS mentor_count
             FROM mentors
             JOIN schools ON mentors.city = schools.city
             GROUP BY schools.country
             ORDER BY schools.country;"""
    result = database.handle_data(query)
    return result


def get_contacts():
    query = """SELECT schools.name, mentors.first_name, mentors.last_name
             FROM mentors
             RIGHT JOIN schools ON mentors.id = schools.contact_person
             ORDER BY schools.name;"""
    result = database.handle_data(query)
    return result


def get_applicants_by_creation():
    query = """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
             FROM applicants
             JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
             WHERE applicants_mentors.creation_date > '2016-01-01'
             ORDER BY applicants_mentors.creation_date DESC;"""
    result = database.handle_data(query)
    return result


def get_applicants_and_mentors():
    query = """SELECT a.first_name AS applicant_first, a.application_code,
                    m.first_name AS mentor_first , m.last_name AS mentor_last
             FROM applicants a
             LEFT JOIN applicants_mentors am ON am.applicant_id = a.id
             LEFT JOIN mentors m ON m.id = am.mentor_id
             ORDER BY a.id;"""
    result = database.handle_data(query)
    return result