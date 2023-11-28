from .until import get_value


def get_detail_of_course(self, iid_course):
    payload = {
        "ntype": "course",
        "depth": 2,
        "is_preview": "false",
        "editing_syllabus": 2,
        "iid": iid_course,
    }
    response = self.send("/api/v2/syllabus/get", payload)
    print(f"Course: {iid_course} - {response['result']['name']}")
    return get_value(response, "result")


def get_member_of_course(self, iid_course):
    payload = {"item_iid": iid_course, "items_per_page": "-1", "page": "1"}
    response = self.send("/course/member/search", payload)
    response = get_value(response, "result")
    list_user = (
        [
            {
                "iid": item["user"]["iid"],
                "code": item["user"]["code"],
                "name": item["user"]["name"],
            }
            for item in response
        ]
        if response
        else []
    )

    print(f"Đã load thông tin của {len(list_user)} học viên")
    return list_user


def get_list_course_of_ep(self, iid_ep):
    payload = {
        "_sand_get_total": 1,
        "_sand_step": "enrolment_plan",
        "enrolment_plans": iid_ep,
    }
    response = self.send("/course/my", payload)
    result = get_value(response, "result")
    if result:
        print(f"Đã load thông tin {len(result)} course của ep {iid_ep}")
        return result
    else:
        print(f"{iid_ep} không có course nào")
        return []


def create_contest(self, iid_course):
    payload = {"iid": iid_course}
    response = self.send("/course/contest/create-contest", payload)
    print(response)


def delete(self, id_course):
    payload = {"id": id_course}
    response = self.send("/course/delete", payload)
    print(response["message"])
