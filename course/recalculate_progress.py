import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.course import recalculate_progress

school = lms.New(dmn="ve", type_dmn="th", user_code="hoanx")
recalculate_progress(school, iid_course=132693196, iid_user=675569)
