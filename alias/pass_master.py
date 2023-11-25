import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.until import get_value_of_index_in_list

dmn = sys.argv[1]
new_pass_master = get_value_of_index_in_list(sys.argv, 2)
type_dmn = get_value_of_index_in_list(sys.argv, 3, default="alpha")
school = lms.New(type=type_dmn, dmn=dmn, user_code="root", password="qWe123!@#QwE")
school.set_pass_master(new_pass_master) if new_pass_master else school.get_pass_master()
