from .until import save_file, clear_file_name, get_value
from .attendance import get_url_file_import_attendance
from .session import get_session_of_course, attendance_one_user


class New:
    def __init__(self, school, iid_course) -> None:
        self.school = school
        self.iid = iid_course
        self.detail = get_detail_of_course(self.school, self.iid)
        self.users = get_member_of_course(self.school, self.iid)
        self.sessions = get_session_of_course(self.school, self.iid)
        self.syllabus_iid = self.detail["syllabus"]

    def download_file_import_attendance(self, folder_path):
        file_name = clear_file_name(self.detail["name"])
        full_name = f"{self.iid} - {file_name}.xlsx"
        url_file = get_url_file_import_attendance(self.school, self.iid)
        save_file(url_file, folder_path, full_name)

    def attentdent_all(self):
        for session in self.sessions:
            for user in self.users:
                attendance_one_user(self.school, self.iid, session, user)


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
    return response["result"]


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
