import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.syllabus import clone_syllabus

# list syllabus kỹ năng mềm
list_syllabus = [
    6273014,
    9496333,
    9496418,
    9496444,
    9499663,
    9499708,
    9888596,
    9918220,
    9918240,
    9918255,
    9918269,
]
target_dmn = "koffmann"
school = lms.New(dmn="khachhang", user_code="root")
for iid_syllabus in list_syllabus:
    clone_syllabus(school, target_dmn, iid_syllabus)
