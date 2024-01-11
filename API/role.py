from .until import get_value


def add_role_to_course(self, iid_course, iid_role):
    payload = {
        "abstractIids[0]": iid_role,
        "type": "course",
        "applied_target_iid": iid_course,
    }
    response = self.send("/abac-role/new-from-abstract", payload)
    print(response)


def get_list_role_can_use_of_organization(self, iid_org):
    payload = {"type": "school", "sub_type": 1, "applied_target_iid": iid_org}
    response = self.send(
        "/abac-role/api/get-abstract-roles-options-for-specific-role-type", payload
    )
    response = get_value(input_data=response, key="result", default=[])
    return response


def get_list_role_applied_of_organization(self, iid_org):
    payload = {
        "_sand_get_total": 1,
        "_sand_step": "school",
        "type": "school",
        "applied_target_iid": iid_org,
        "page": 1,
        "items_per_page": "-1",
    }
    response = self.send("/abac-role/search", payload)
    response = get_value(input_data=response, key="result", default=[])
    return response


def apply_role_to_organization(self, iid_role, iid_org):
    payload = {
        "abstractIids[0]": iid_role,
        "type": "school",
        "applied_target_iid": iid_org,
    }
    response = self.send("/abac-role/new-from-abstract", payload)
    if response["success"]:
        print(f"Đã add role {iid_role} cho org {iid_org}")


def hanlder_apply_role_to_organization(self, name_role, iid_org):
    name_role = name_role.lower()
    list_role_applied_of_organization = get_list_role_applied_of_organization(
        self, iid_org
    )
    for i in list_role_applied_of_organization:
        if i["name"].lower() == name_role:
            return True
    list_role_can_use_of_organization = get_list_role_can_use_of_organization(
        self, iid_org
    )
    for i in list_role_can_use_of_organization:
        if i["name"].lower() == name_role:
            apply_role_to_organization(self, iid_role=i["iid"], iid_org=iid_org)
            return True
    return False


def get_role_can_add_to_course(self, iid_course):
    payload = {"applied_target_iid": iid_course, "type": "course"}
    response = self.send("/abac-role/api/get-role-options", payload)
    return get_value(input_data=response, key="result", default=[])


def get_role_can_apply_for_user(self, iid_user, iid_org):
    payload = {
        "user_iid": iid_user,
        "applied_target_iid": iid_org,
        "fetchRoleOptionParams[type]": "school",
        "fetchRoleOptionParams[applied_target_iid]": iid_org,
        "type": "school",
    }
    response = self.send("/abac-role/api/get-role-options", payload)
    return get_value(input_data=response, key="result", default=[])


def get_role_applied_of_user(self, iid_user, applied_target_iid):
    payload = {"applied_target_iid": applied_target_iid, "user_iid": iid_user}
    response = self.send(
        "/user-abac-role/api/get-roles-of-user-in-applied-target", payload
    )
    return get_value(input_data=response, key="result", default=[])


def update_role_for_user(self, iid_user, iid_applied_target, idd_roles):
    payload = {
        "user_iid": iid_user,
        "applied_target_iid": iid_applied_target,
        "fetchRoleOptionParams[type]": "school",
        "fetchRoleOptionParams[applied_target_iid]": iid_applied_target,
    }
    for idx, idd_role in enumerate(idd_roles):
        payload.update({f"role_iids[{idx}]": idd_role})
    response = self.send("/user-abac-role/update", payload)
    print(response)
