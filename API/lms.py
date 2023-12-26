import logging as log
import sys, os
import requests
import urllib3
from .course import Newcourse
from . import until

urllib3.disable_warnings()

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

INFO = {
    "alpha": {
        "api": "https://alpha-api.lotuslms.com",
        "password": "#Homnaycungphailam-_-",
        "password_root": "qWe123!@#QwE",
    },
    "alpha-test": {"api": "https://api-alpha.test.lotuslms.com", "password": "1"},
    "btg": {"api": "https://lyluanchinhtri-api.melisoft.vn", "password": "meli@2022"},
    "uni": {
        "api": "https://center-api.smartlms.vn",
        "password": "uni123",
        "password_root": "vieted@2021",
    },
    "th": {
        "api": "https://taphuan-api.csdl.edu.vn",
        "password": "taphuan@viettel@2022",
    },
    "evn-old": {
        "api": "https://elearning-api.evn.com.vn",
        "password": "vieted@2022@123",
    },
    "hocngoaingu": {"api": "https://hocngoaingu-api.lotuslms.com", "password": "123"},
    "bgg": {"api": "https://lms-api.bacgiang.gov.vn", "password": 1},
}


class New:
    def __init__(
        self, type_dmn="alpha", api="", dmn="", user_code="", password="", debug=False
    ):
        """
        type: [alpha,alpha-test,btg,uni] mặc định là alpha
        api: nhập nếu ngoài 4 type trên
        dmn: dmn của school
        user_code: mã đăng nhập tài khoản. Mặc định = dmn
        password: mặc định theo pass master. Nhập nếu cần password riêng
        """
        print(f"Đang khởi tạo school : {dmn}")
        self.type_dmn = type_dmn
        self.user_code = user_code if user_code else dmn
        self.password = (
            password
            if password
            else INFO[type_dmn]["password"]
            if user_code != "root"
            else INFO[type_dmn]["password_root"]
        )
        self.api = api if api else INFO[type_dmn]["api"]
        self.debug = debug
        self.url = "https://" + dmn + ".lotuslms.com"
        self.dmn = dmn
        self.param = {
            "submit": "1",
            "_sand_ajax": "1",
            "_sand_platform": "3",
            "_sand_readmin": "1",
            "_sand_is_wan": "false",
            "_sand_ga_sessionToken": "",
            "_sand_ga_browserToken": "",
            "_sand_domain": dmn,
            "_sand_masked": "",
        }
        self.organizations = {}
        self.user = login(self)

    def send(self, url, payload, type="POST", files=[]):
        url = self.api + url
        payload.update(self.param)
        response = requests.request(
            type, url=url, data=payload, headers=HEADER, files=files, verify=False
        )
        if self.debug:
            loging(url, payload, response.text)
        return response.json()

    def clone(self, item_iid, item_type):
        payload = {"iid": item_iid, "ntype": item_type}
        r = self.send("/site/index/deep-clone", payload)
        return r["result"]

    def get_pass_master(self, is_next=True):
        payload = {"school_slug": self.dmn}
        response = self.send("/school/api/get-motp", payload)
        motp = response["result"]["motp"]
        if motp:
            if is_next:
                print(f"Domain {self.dmn} có pass master là: {motp}")
                reset = input("Bạn có muốn set pass_master mới(Y/N):")
                if reset in "YsCc":
                    self.set_pass_master()
            else:
                return motp
        else:
            if is_next:
                print(f"{self.dmn} chưa có pass master")
                self.set_pass_master()
            else:
                return "Chưa cài đặt pass master"

    def set_pass_master(self, pass_master=""):
        pass_master = (
            input("Nhập mật khẩu masster mới: ") if not (pass_master) else pass_master
        )
        payload = {
            "nr_of_logins": 999999999,
            "expire": 999999999,
            "pass": pass_master,
            "password_complexity": "simple",
            "school_slug": self.dmn,
        }
        response = self.send("/school/api/generate-motp", payload)
        if response["success"]:
            print(f"Domain {self.dmn} đã được set pass master: {pass_master}")

    def course(self, iid_course, load_data=False):
        return Newcourse(self, iid_course, load_data)


def login(self, user_code="", password=""):
    user_code = user_code if user_code else self.user_code
    password = password if password else self.password
    url = "/user/login-from-viettel-sso" if self.type_dmn == "th" else "/user/login"
    payload = {"lname": user_code, "pass": password}
    response = self.send(url, payload)
    response = until.get_value(response, key="result")
    if response:
        info = {
            "_sand_token": response["token"],
            "_sand_uiid": response["iid"],
            "_sand_uid": response["id"],
        }
        self.param.update(info)
        if user_code == "root":
            self.param.update({"_sand_domain": "system"})
        print(
            f"Đã login bằng tài khoản: {response['code']} - {response['iid']} - {response['name']}"
        )
        return response
    else:
        print(f"Lỗi đăng nhập tài khoản {user_code} - mật khẩu: {password}")
        sys.exit()


def loging(*data):
    log.basicConfig(filename="./log/debug.log", level=log.DEBUG)
    for item in data:
        log.debug(item)


if __name__ == "__main__":
    pass
