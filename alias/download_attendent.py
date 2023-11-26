import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms, course
from API.until import get_path_full, open_folder

dmn = sys.argv[1]
iid_course = sys.argv[2]

school = lms.New(dmn=dmn, debug=True)
course_target = course.New(school, iid_course)
folder_path = get_path_full("session\import")
course_target.download_file_import_attendance(folder_path)
open_folder(folder_path)
