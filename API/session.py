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
    try:
        print(f"Đã load thông tin {response['count']} buổi học")
        return response["result"]
    except:
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
    if response["success"]:
        print(session["name"], " > ", user["name"])
    else:
        print("lỗi")
