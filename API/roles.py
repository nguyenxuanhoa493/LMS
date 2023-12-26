def set_roles(self, iid_course, iid_role):
    payload = {
        "abstractIids[0]": iid_role,
        "type": "course",
        "applied_target_iid": iid_course,
    }
    response = self.send("/abac-role/new-from-abstract", payload)
    print(response)
