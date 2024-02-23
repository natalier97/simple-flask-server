from flask import Flask
from data import students


app = Flask(__name__)

#Returns an array of student objects where the students are older than 20 years old.
@app.route('/old_students/', methods=['GET'])
def get_old_students():
    old_stud = []
    for stud_obj in students:
        if stud_obj.get('age') > 20:
            old_stud.append(stud_obj)
    return old_stud


#/young_students/: Returns an array of student objects where the students are younger than 21 years old.
@app.route('/young_students/', methods=['GET'])
def get_young_students():
    young_stud = []
    for stud_obj in students:
        if stud_obj.get('age') < 21:
            young_stud.append(stud_obj)
    return young_stud



#/advance_students/: Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
@app.route('/advance_students/', methods=['GET'])
def get_advance_students():
    advance_stud = []
    young_stud = get_young_students()
    for stud_obj in young_stud:
        if stud_obj.get('grade') == 'A':
            advance_stud.append(stud_obj)
    return advance_stud


#/student_names/: Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
@app.route('/student_names/', methods=['GET'])
def get_student_names():
    name_array = []
    for stud_obj in students:
        name_dict = {}
        name_dict['first_name'] = stud_obj.get('first_name')
        name_dict['last_name'] = stud_obj.get('last_name')
        name_array.append(name_dict)
    return name_array





#/student_ages/: Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
@app.route('/student_ages/', methods=['GET'])
def get_student_ages():
    age_array = []
    for stud_obj in students:
        age_dict = {}
        age_dict['name'] = stud_obj.get('first_name'), stud_obj.get('last_name')
        age_dict['age'] = stud_obj.get('age')
        age_array.append(age_dict)
    return age_array






#/students/: Returns an array of all student objects available.
@app.route('/students/', methods=['GET'])
def get_students():
    return students




if __name__ == '__main__':
    app.run(debug=True)