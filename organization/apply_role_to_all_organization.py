import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.role import hanlder_apply_role_to_organization
from API.organization import get_list_children_of_organization

school = lms.New(dmn="khl")
name_role = "test 2"
iid_org = 2397331


def apply_role(name_role, iid_org):
    global school
    is_applied_role = hanlder_apply_role_to_organization(school, name_role, iid_org)
    if not (is_applied_role):
        print(f"Không tìm thấy quyền: {name_role}")
        return False
    sub_organizations = get_list_children_of_organization(school, iid_org)
    for org in sub_organizations:
        apply_role(name_role, iid_org=org["iid"])


apply_role(name_role, iid_org)
