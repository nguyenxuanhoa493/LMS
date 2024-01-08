import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.survey import add_surveys_to_applied_item

school = lms.New(dmn="xanhsm", user_code="gsm")

list_survey = [13234148]
list_syllabus = [13233707]
for syllabus in list_syllabus:
    for survey in list_survey:
        add_surveys_to_applied_item(school, syllabus, survey)
