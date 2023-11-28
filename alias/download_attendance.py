import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms, course
from API.until import get_path_full, open_folder, get_value

dmn = sys.argv[1]
school = lms.New(dmn=dmn)
list_iid = sys.argv[2].split(",")
type_target = get_value(sys.argv, key=3, default="course")
if type_target == "ep":
    list_target = [course.get_list_course_of_ep(school, iid_ep) for iid_ep in list_iid]
    list_target = [item["iid"] for sublist in list_target for item in sublist]
else:
    list_target = list_iid

folder_path = get_path_full("session/import")
for iid_course in list_target:
    course_target = school.course(iid_course, load_data=True)
    course_target.download_file_import_attendance(folder_path)
open_folder(folder_path)
