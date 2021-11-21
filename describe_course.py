# example of how to get a template to work
from jinja2 import Environment, FileSystemLoader

course1 = {
    'title': 'MUSA 509: Geospatial Cloud Computing',
    'is_virtual': False,
    'room': 'GSE 114 and virtually',
    'days': 'Monday and Wednesday',
    'instructor_name': 'Mjumbe Poe',
    'student_names': ['Jeff', 'Jeff', 'Jeff', 'jeff']
}

env = Environment(loader=FileSystemLoader('/Users/jeffstern/Documents/UPenn/Courses/MUSA-509/final-project/templates/'))
template = env.get_template('station.html')
output = template.render(course=course1)

file = open("sample.html","w")
file.write(output)
file.close()
