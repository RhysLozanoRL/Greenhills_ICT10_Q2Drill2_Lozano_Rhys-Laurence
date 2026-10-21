# Working with Sets 
from pyscript import display, document # type: ignore

def student_members(e):
    grade_7 = {'Georgina Sarmiento', 'Elianna Co'}
    grade_8 = {'Miishka Eugenio', 'Aiva Suson'}
    grade_9 = {'Mallorie Micu', 'Liesl Pascual'}
    grade_10 = {'Savannah Reyes', 'Zoe Reyes'}

    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    student_fullname = firstname + ' ' + lastname

    members = grade_7.union(grade_8, grade_9, grade_10)

    members.add(student_fullname)
    display("All members : ", members, target='output')

    display("Total number of members now : ", len(members), target='output')




