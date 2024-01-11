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


def delete_session(self, id_session):
    payload = {"id": id_session}
    response = self.send("/session/delete", payload)
    if response["success"]:
        print(f"Đã xoá session: {id_session}")
    else:
        print(response)


def add_new_a_session(self, iid_course, session):
    RANGE_TIME = {
        "Sáng": {
            "scheduled[start_time]": "450",
            "scheduled[end_time]": "690",
            "learn_duration": "240",
        },
        "Chiều": {
            "scheduled[start_time]": "780",
            "scheduled[end_time]": "1020",
            "learn_duration": "240",
        },
        "Tối": {
            "scheduled[start_time]": "1140",
            "scheduled[end_time]": "1380",
            "learn_duration": "240",
        },
    }
    payload = {
        "name": session["name"],
        "scheduled[date_time]": session["date"],
        "enable_recording": "1",
        "location": "ilt_bbb",
        "type": "",
        "count": "1",
        "course_iid": iid_course,
    }
    for idx, iid_teacher in enumerate(session["teacher"]):
        payload.update({f"scheduled[teacher_iids][{idx}]": iid_teacher})
    payload.update(RANGE_TIME[session["time"]])
    response = self.send("POST", "/session/new", payload)
    if response["success"]:
        print(f"Đã tạo buổi học: {session['date']} - {session['name']}")
    else:
        print(response)
