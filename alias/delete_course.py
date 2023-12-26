import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.until import get_value

dmn = sys.argv[1]
list_iid = sys.argv[2].split(",")
type_dmn = get_value(sys.argv, key=3, default="alpha")
school = lms.New(type_dmn=type_dmn, dmn=dmn)
for iid_course in list_iid:
    print(iid_course)
    course = school.course(iid_course=iid_course, load_data=True)
    course.delete()
