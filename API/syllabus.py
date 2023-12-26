from .until import get_value


def detail(self, iid_syllabus):
    payload = {
        "ntype": "syllabus",
        "depth": "-1",
        "is_preview": 1,
        "editing_syllabus": 2,
        "iid": iid_syllabus,
    }
    response = self.send("/api/v2/syllabus/get", payload)
    result = get_value(response, key="result")
    if result:
        print(
            f"Đã load thông tin syllabus {iid_syllabus} - {response['result']['name']}"
        )
        return get_value(response, key="result")


def get_link_content(self, iid_syllabus):
    return f"{self.api}/api/v2/syllabus/get?ntype=syllabus&depth=-1&is_preview=true&editing_syllabus=2&iid={iid_syllabus}&submit=1&_sand_ajax=1&_sand_platform=3&_sand_readmin=1&_sand_is_wan=false&_sand_ga_sessionToken=&_sand_ga_browserToken=&_sand_domain={self.dmn}&_sand_masked=&_sand_token={self.user['token']}&_sand_uiid={self.user['iid']}&_sand_uid={self.user['id']}"


def clone_syllabus_from_api(self, orl_school="", iid_syllabus="", api_get=""):
    api_to_get = api_get if api_get else get_link_content(orl_school, iid_syllabus)
    payload = {"api_to_get_data": api_to_get}
    response = self.send("/school/api/deep-clone-data-from-api", payload)
    print(response)
    result = get_value(response, key="result")
    return result if result else False


def clone_syllabus(self, target_dmn, iid_syllabus):
    payload = {
        "syllabus_iid": iid_syllabus,
        "target_school": target_dmn,
        "origin_school": self.dmn,
    }

    response = self.send("/store/site/copy-syllabus", payload)
    if response["success"]:
        return response["result"]
    else:
        print(f"Lỗi {iid_syllabus}")
        print(response)


def approved(self, id_syllabus):
    payload = {
        "id": id_syllabus,
        "_sand_step": "status",
        "type": "credit",
        "status": "approved",
    }
    r = self.send("/syllabus/update", payload)
    print(r["message"])
