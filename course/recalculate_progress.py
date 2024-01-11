import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.course import recalculate_progress

school = lms.New(dmn="xanhsm", user_code="gsm")
recalculate_progress(school, iid_course=13287701, iid_user=712282)
