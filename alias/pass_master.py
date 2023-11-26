import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.until import get_value

type_dmn = get_value(sys.argv, key=1)
dmn = sys.argv[2]
new_pass_master = get_value(sys.argv, key=3)
school = lms.New(type_dmn=type_dmn, dmn=dmn, user_code="root")
school.set_pass_master(new_pass_master) if new_pass_master else school.get_pass_master()
