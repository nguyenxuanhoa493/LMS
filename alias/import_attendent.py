import sys, os, re

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.file import upload
from API.attendance import get_import_id, import_attendance

# truyền vào dmn và  ds link import điểm danh
dmn = sys.argv[1]
list_file = sys.argv[2]
list_file = list_file = sys.argv[2].split(",")

school = lms.New(dmn=dmn)
for file in list_file:
    file_name = os.path.basename(file)
    iid_course = re.search(r"\d+", file_name)[0]
    file_uploaded = upload(school, file)
    import_id = get_import_id(school, file_uploaded, iid_course)
    import_attendance(school, import_id, iid_course)
