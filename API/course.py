from random import randint
import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import syllabus, attendance, until, session, file, lms


class Newcourse:
    def __init__(self, school, iid_course, load_data):
        self.school = school
        self.iid = iid_course
        if load_data:
            self.detail = get_detail_of_course(self.school, self.iid)
            self.syllabus = syllabus.get_detail_of_syllabus(
                self.school, iid_syllabus=self.detail["syllabus"]
            )
            self.users = get_member_of_course(self.school, self.iid)
            self.sessions = session.get_session_of_course(self.school, self.iid)

    def download_file_import_attendance(self, folder_path):
        file_name = until.clear_file_name(self.detail["name"])
        full_name = f"{self.iid} _ {file_name}.xlsx"
        url_file = attendance.get_url_file_import_attendance(self.school, self.iid)
        until.save_file(url_file, folder_path, full_name)

    def import_attendance(self, file_import):
        file_uploaded = file.upload(self.school, file_import)
        import_id = attendance.get_import_id(
            self.school, file_uploaded["link"], self.iid
        )
        attendance.import_attendance(self.school, import_id, self.iid)

    def attentdent(self, list_user=[]):
        for s in self.sessions:
            for u in self.users:
                if (list_user and u["iid"] in list_user) or not list_user:
                    session.attendance_one_user(self.school, self.iid, s, u)

    def create_contest(self):
        create_contest(self.school, self.iid)

    def delete_member(self):
        delete_member(self.school, self.users, self.iid)

    def delete(self):
        if self.users:
            self.delete_member()
        delete(self.school, self.detail["id"])

    def auto_learn(
        self,
        user_code,
        progress_min=100,
        progress_max=100,
        spent_time_min=400,
        spent_time_max=1000,
    ):
        content = self.syllabus["children"]
        lms.login(self.school, user_code)
        learn(
            self.school,
            content=content,
            iid_course=self.iid,
            progress_min=progress_min,
            progress_max=progress_max,
            spent_time_min=spent_time_min,
            spent_time_max=spent_time_max,
        )

    def resync_score(self):
        resync_score(self.school, self.iid)


def get_detail_of_course(self, iid_course):
    payload = {
        "ntype": "course",
        "depth": 2,
        "is_preview": "false",
        "editing_syllabus": 2,
        "iid": iid_course,
    }
    response = self.send("/api/v2/syllabus/get", payload)
    response = until.get_value(response, key="result")
    print(f"Course: {iid_course} _ {response['name']}")
    return response


def get_member_of_course(self, iid_course):
    payload = {"item_iid": iid_course, "items_per_page": "_1", "page": "1"}
    response = self.send("/course/member/search", payload)
    list_user = []
    response = until.get_value(response, key="result")
    if response:
        for item in response:
            list_user.append(
                {
                    "id": item["_id"],
                    "iid": item["user"]["iid"],
                    "code": item["user"]["code"],
                    "name": item["user"]["name"],
                }
            )
    print(f"Đã load thông tin của {len(list_user)} học viên của khoá học")
    return list_user


def get_list_course_of_ep(self, iid_ep):
    payload = {
        "_sand_get_total": 1,
        "_sand_step": "enrolment_plan",
        "enrolment_plans": iid_ep,
    }
    response = self.send("/course/my", payload)
    response = until.get_value(response, key="result", default=[])
    if response:
        print(f"Đã load thông tin {len(response)} course của ep {iid_ep}")
        return response
    else:
        print(f"{iid_ep} không có course nào")
        return []


def create_contest(self, iid_course):
    payload = {"iid": iid_course}
    response = self.send("/course/contest/create_contest", payload)
    print(response)


def delete(self, id_course):
    payload = {"id": id_course}
    response = self.send("/course/delete", payload)
    print(response)


def set_rubric(self, course, iid_rubric):
    payload = {
        "iid": course["iid"],
        "id": course["id"],
        "ntype": "course",
        "rubric_iid": iid_rubric,
        "_sand_step": "rubric",
    }
    response = self.send("/course/update", payload)
    print(response)


def new(self, payload):
    response = self.send("/course/new", payload)
    return response["result"]


def update_status(self, id_course, status="approved"):
    payload = {"id": id_course, "_sand_step": "status", "status": status}
    response = self.send("/course/update", payload)
    print(f"{id_course} | {response}")


def add_member(self, list_user, iid_course):
    payload = {"mode": "add", "iid": iid_course}
    for idx, user in enumerate(list_user):
        uiid = until.get_value(user, key="iid", default=user)
        payload.update({f"user_iids[{idx}]": uiid})
    response = self.send("/course/enrol/add_members", payload)
    print(response)


def delete_member(self, list_user, iid_course):
    payload = {"act": "delete", "nodeIid": iid_course}
    for idx, user in enumerate(list_user):
        payload.update({f"ids[{idx}]": user["id"]})
    response = self.send("/course/enrol/delete", payload)
    if response["success"]:
        print(f"Đã xoá {len(list_user)} user khỏi khoá học {iid_course}")


def resync_score(self, iid_course):
    payload = {
        "sync_options[0]": "progress_course",
        "iid": iid_course,
    }
    self.send("/course/progress/sync_course_progress_by_rubrik", payload)


def save_progress(self, iid_course, item, progress=100, spent_time=500):
    item_type = None
    item_name = ""
    try:
        item_type = item.get("type", None)
        item_name = item.get("name", None)
        item_iid = item["iid"]
    except:
        item_iid = item

    param_video = {
        "progress[0][tco_iid]": item_iid,
        "progress[0][p]": progress,
        "progress[0][pd][n]": "10",
        "progress[0][pd][i][0]": "0",
        "progress[0][pd][i][1]": "1",
        "progress[0][pd][i][2]": "2",
        "progress[0][pd][i][3]": "3",
        "progress[0][pd][i][4]": "4",
        "progress[0][pd][i][5]": "5",
        "progress[0][pd][i][6]": "6",
        "progress[0][pd][i][7]": "7",
        "progress[0][pd][i][8]": "8",
        "progress[0][pd][i][9]": "9",
        "progress[0][time_spent]": spent_time,
        "ciid": iid_course,
    }

    param_other = {
        "progress[0][tco_iid]": item_iid,
        "progress[0][p]": progress,
        "progress[0][time_spent]": spent_time,
        "ciid": iid_course,
    }

    payload = param_video if item_type == "video" else param_other
    response = self.send("/trckr2/save", payload)
    print(f"[{item_type}] _ {item_name}") if response["success"] else print("Lỗi")


def learn(
    self,
    content,
    iid_course,
    progress_min=100,
    progress_max=100,
    spent_time_min=400,
    spent_time_max=1200,
):
    for item in content:
        tpl_type = item.get("tpl_type", None)
        progress = randint(progress_min, progress_max)
        spent_time = randint(spent_time_min, spent_time_max)
        if tpl_type == "standard":
            learn(
                self,
                item["children"],
                iid_course,
                progress_min,
                progress_max,
                spent_time_min,
                spent_time_max,
            )
        else:
            save_progress(self, iid_course, item, progress, spent_time)


def recalculate_progress(self, iid_course, iid_user):
    payload = {"course_iid": iid_course, "user_iid": iid_user}
    self.send("/course/progress/recalculate_course_users_progress", payload)


def create_sessions_from_template(self, iid_course):
    payload = {"course_iid": iid_course}
    response = self.send("/course/session/create-sessions-from-template", payload)
    print(response)
