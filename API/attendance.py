def get_import_id(self, attachments, iid_course):
    payload = {"import_file": attachments["link"], "course_iid": iid_course}
    response = self.send("/attendance/import/import", payload)
    return response["result"]["import_id"]


def import_attendance(self, import_id, iid_course):
    payload = {"importId": import_id, "course_iid": iid_course}
    response = self.send("/attendance/import/process", payload)
    print(f"{response['message']} > {iid_course}")
