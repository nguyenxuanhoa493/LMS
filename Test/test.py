import sys, os, json

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms, course

school = lms.New(dmn="testvieted", debug=True)
course_test = course.New(school, 12771932)
course_of_ep = course.get_list_course_of_ep(school, 12772111)
