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
