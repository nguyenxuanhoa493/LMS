import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms

school = lms.New(dmn="bvl", user_code="root")
