from .until import get_value


def search(self, iid_org):
    payload = {
        "_sand_get_total": 1,
        "textOp": "$like",
        "include_sub_organizations": 0,
        "user_organizations[0]": iid_org,
        "ntype": "user",
        "_sand_step": "students",
    }
    response = self.send("/user/api/search", payload)
    return get_value(response, "result")


def handler_staff_of_user(self, iid_user, iid_org, status="add"):
    # status: add or kickout
    payload = {"userIid": iid_user, "user_organizations[0]": iid_org, "status": status}
    self.send("/school/add-staff", payload)


def get_detail_user(self, iid_user):
    payload = {"ntype": "user", "editing_syllabus": "1", "iid": iid_user}
    response = self.send("/user/detail", payload)
    return get_value(input_data=response, key="result", default=False)
