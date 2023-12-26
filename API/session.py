from .until import get_value


def get_detail_session(self, iid_session):
    payload = {"iid": iid_session}
    response = self.send("/session/api/get-detail", payload)
    return response["result"]


def get_session_of_course(self, iid_course, status="123"):
    """
    Status:
    1: Hoàn thành
    2: Đang diễn ra
    3: Sắp diễn ra
    """
    payload = {
        "course_iid": iid_course,
        "page": 1,
        "items_per_page": -1,
    }
    for idx, val in enumerate(status):
        payload.update({f"session_status[{idx}]": val})
    response = self.send("/session/search", payload)
    response = get_value(response, key="result")
    if response:
        print(f"Đã load thông tin {len(response)} buổi học")
        return response
    else:
        print(f"Course {iid_course} chưa tạo buổi học")
        return []


def attendance_one_user(self, iid_course, session, user, status=1):
    payload = {
        "type": "session_for_user",
        "course_iid": iid_course,
        "ntype": "session",
        "iid": session["iid"],
        "id": session["id"],
        "_sand_step": "attendance",
        "attendance[status]": status,
        "attendance[user_iid]": user["iid"],
    }
    response = self.send("/session/update", payload)
    print(session["name"], " > ", user["name"])
