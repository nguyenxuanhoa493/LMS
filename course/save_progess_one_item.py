import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.course import save_progress

school = lms.New(dmn="xanhsm", user_code="00107228309")
save_progress(school, iid_course=13287701, item={"iid": 13314830, "type": "video"})
