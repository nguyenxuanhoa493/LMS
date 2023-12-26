from .until import get_ts_now


def new(self, name_academic, code_academic=get_ts_now(), pid=""):
    payload = {
        "type": "academic",
        "name": name_academic,
        "code": code_academic,
        "pid": pid,
        "status": "init",
    }
    response = self.send("/category/index/new", payload)
    return response["result"]
