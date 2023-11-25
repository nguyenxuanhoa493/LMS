from .until import save_file, clear_file_name


class New:
    def __init__(self, school, iid_course) -> None:
        self.school = school
        self.iid = iid_course
        self.detail = {}
        self.user = {}
        self.sessions = {}
        self.syllabus_iid = 0

    def load_detail(self):
        self.detail = detail(self.school, self.iid)
        self.syllabus_iid = self.detail["syllabus"]

    def load_users(self):
        self.users = users(self.school, self.iid)

    def load_sessions(self, status="123"):
        """
        Status:
        1: Hoàn thành
        2: Đang diễn ra
        3: Sắp diễn ra
        """
        self.sessions = sessions(self.school, self.iid, status)

    def download_file_import_attendance(self, folder_path):
        self.load_detail()
        file_name = clear_file_name(self.detail["name"])
        full_name = f"{self.iid} - {file_name}.xlsx"
        url_file = get_url_file_import_attendance(self.school, self.iid)
        save_file(url_file, folder_path, full_name)


def detail(self, iid_course):
    payload = {
        "ntype": "course",
        "depth": 2,
        "is_preview": "false",
        "editing_syllabus": 2,
        "iid": iid_course,
    }
    response = self.send("/api/v2/syllabus/get", payload)
    print(f"Course: {iid_course} - {response['result']['name']}")
    return response["result"]


def users(self, iid_course):
    payload = {"item_iid": iid_course, "items_per_page": "-1", "page": "1"}
    response = self.send("/course/member/search", payload)
    list_user = []
    try:
        for r in response["result"]:
            list_user.append(
                {
                    "iid": r["user"]["iid"],
                    "code": r["user"]["code"],
                    "name": r["user"]["name"],
                }
            )
        print(f"Đã load thông tin của {len(list_user)} học viên")
        return list_user
    except:
        print("Course chưa có học viên")
        return []


def sessions(self, iid_course, status="123"):
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


def get_url_file_import_attendance(self, iid_course):
    payload = {
        "type": "attendance",
        "template": "import_attendance",
        "course_iid": iid_course,
    }
    response = self.send("/import/data/download-template-to-import", payload)
    return response["objects"]["url"]
