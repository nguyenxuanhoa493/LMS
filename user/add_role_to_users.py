import sys
from os.path import join, dirname
import re

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.role import (
    get_role_can_apply_for_user,
    get_role_applied_of_user,
    update_role_for_user,
)
from API.user import handler_staff_of_user

data = [
    {
        "code": "L1009060521",
        "iid": 687808,
        "id": "65373976ee60bd2f11160557",
        "name": "Nguyễn Hoàng Hải",
        "user_organizations": 2173002,
        "roles": 2,
    },
    {
        "code": "L1007130367",
        "iid": 298409,
        "id": "61c8385e3ea13c74b9141ef5",
        "name": "Nguyễn Hoàng Anh",
        "user_organizations": 2173004,
        "roles": 2,
    },
    {
        "code": "L1007300363",
        "iid": 298370,
        "id": "61c838583ea13c74b9141ece",
        "name": "Trần Phi Hùng",
        "user_organizations": 2172995,
        "roles": 2,
    },
    {
        "code": "L1007300477",
        "iid": 298322,
        "id": "61c838513ea13c74b9141e9e",
        "name": "Lê Xuân Ngọ",
        "user_organizations": 2173001,
        "roles": 2,
    },
    {
        "code": "L1007290403",
        "iid": 298299,
        "id": "61c8384e3ea13c74b9141e87",
        "name": "Nông Anh Tuấn",
        "user_organizations": 2173000,
        "roles": 2,
    },
    {
        "code": "L1007140350",
        "iid": 298280,
        "id": "61c8384b3ea13c74b9141e74",
        "name": "Trịnh Hồng Minh",
        "user_organizations": 2172999,
        "roles": 2,
    },
    {
        "code": "L1108050594",
        "iid": 298252,
        "id": "61c838473ea13c74b9141e58",
        "name": "Nguyễn Đình Quân",
        "user_organizations": 2172978,
        "roles": 2,
    },
    {
        "code": "L1007260382",
        "iid": 298235,
        "id": "61c838453ea13c74b9141e47",
        "name": "Trần Đức Ngọc",
        "user_organizations": 2172994,
        "roles": 2,
    },
    {
        "code": "L1007280372",
        "iid": 298205,
        "id": "61c838413ea13c74b9141e29",
        "name": "Nguyễn Thị Loan",
        "user_organizations": 2172992,
        "roles": 2,
    },
    {
        "code": "L1108050595",
        "iid": 298187,
        "id": "61c8383e3ea13c74b9141e17",
        "name": "Nguyễn Hữu Tuấn",
        "user_organizations": 2172991,
        "roles": 2,
    },
    {
        "code": "L1510022139",
        "iid": 298149,
        "id": "61c838393ea13c74b9141df1",
        "name": "Nguyễn Minh Vương",
        "user_organizations": 2172989,
        "roles": 2,
    },
    {
        "code": "L1007210409",
        "iid": 298125,
        "id": "61c838363ea13c74b9141dd9",
        "name": "Lê Quang Hòa",
        "user_organizations": 2172988,
        "roles": 2,
    },
    {
        "code": "L1009010379",
        "iid": 298104,
        "id": "61c838333ea13c74b9141dc4",
        "name": "Hồ Thị Hạnh",
        "user_organizations": 2172986,
        "roles": 2,
    },
    {
        "code": "L1009060490",
        "iid": 297963,
        "id": "61c8381f3ea13c74b9141d37",
        "name": "Nguyễn Công Chính",
        "user_organizations": 2172979,
        "roles": 2,
    },
    {
        "code": "L1007300381",
        "iid": 297954,
        "id": "61c8381e3ea13c74b9141d2e",
        "name": "Nguyễn Xuân Thông",
        "user_organizations": 2172959,
        "roles": 2,
    },
    {
        "code": "L1007260355",
        "iid": 297923,
        "id": "61c838193ea13c74b9141d0f",
        "name": "Nguyễn Chí Bắc",
        "user_organizations": 2172980,
        "roles": 2,
    },
    {
        "code": "L1802223808",
        "iid": 297836,
        "id": "61c8380d3ea13c74b9141cb8",
        "name": "Nguyễn Viết Hưng",
        "user_organizations": 2172972,
        "roles": 2,
    },
    {
        "code": "L1007290366",
        "iid": 297826,
        "id": "61c8380c3ea13c74b9141cae",
        "name": "Trần Văn Xuân",
        "user_organizations": 2172971,
        "roles": 2,
    },
    {
        "code": "L1007200360",
        "iid": 297800,
        "id": "61c838083ea13c74b9141c94",
        "name": "Ngô Minh Đức",
        "user_organizations": 2172973,
        "roles": 2,
    },
    {
        "code": "L1007220351",
        "iid": 297740,
        "id": "61c838003ea13c74b9141c58",
        "name": "Phạm Thị Thành",
        "user_organizations": 2172969,
        "roles": 2,
    },
    {
        "code": "L1007290429",
        "iid": 297622,
        "id": "61c837ef3ea13c74b9141be2",
        "name": "Bùi Thị Lam Giang",
        "user_organizations": 2172961,
        "roles": 2,
    },
    {
        "code": "L1007210362",
        "iid": 297570,
        "id": "61c837e83ea13c74b9141bae",
        "name": "Nguyễn Gia Thiều",
        "user_organizations": 2172958,
        "roles": 2,
    },
    {
        "code": "L1007280352",
        "iid": 297515,
        "id": "61c837e13ea13c74b9141b77",
        "name": "Nguyễn Thị Ánh Tuyết",
        "user_organizations": 2172955,
        "roles": 2,
    },
    {
        "code": "L1008310410",
        "iid": 297485,
        "id": "61c837dc3ea13c74b9141b59",
        "name": "Lê Thị Minh Phượng",
        "user_organizations": 2172954,
        "roles": 2,
    },
    {
        "code": "L1007140352",
        "iid": 297464,
        "id": "61c837d93ea13c74b9141b44",
        "name": "Ngô Văn Tứ",
        "user_organizations": 2172953,
        "roles": 2,
    },
    {
        "code": "G1306271217",
        "iid": 297455,
        "id": "61c837d83ea13c74b9141b3b",
        "name": "Trần Công Cảnh",
        "user_organizations": 2172952,
        "roles": 2,
    },
    {
        "code": "L1007210469",
        "iid": 297445,
        "id": "61c837d73ea13c74b9141b31",
        "name": "Thái Vũ Quang",
        "user_organizations": 2172951,
        "roles": 2,
    },
    {
        "code": "L1009140440",
        "iid": 297342,
        "id": "61c837c93ea13c74b9141aca",
        "name": "Ngô Văn Phương",
        "user_organizations": 2172945,
        "roles": 2,
    },
    {
        "code": "L1007300447",
        "iid": 297318,
        "id": "61c837c53ea13c74b9141ab2",
        "name": "Đỗ Hoàng Anh",
        "user_organizations": 2172985,
        "roles": 2,
    },
    {
        "code": "L1007080378",
        "iid": 297304,
        "id": "61c837c33ea13c74b9141aa4",
        "name": "Nguyễn Đăng Vũ",
        "user_organizations": 2172942,
        "roles": 2,
    },
    {
        "code": "L1009060369",
        "iid": 297286,
        "id": "61c837c13ea13c74b9141a92",
        "name": "Nguyễn Đình Nhiều",
        "user_organizations": 2172943,
        "roles": 2,
    },
    {
        "code": "L1007300366",
        "iid": 297265,
        "id": "61c837be3ea13c74b9141a7d",
        "name": "Huỳnh Quốc Bảo",
        "user_organizations": 2172941,
        "roles": 2,
    },
    {
        "code": "L1007300467",
        "iid": 297250,
        "id": "61c837bc3ea13c74b9141a6e",
        "name": "Hoàng Việt Phương",
        "user_organizations": 2172940,
        "roles": 2,
    },
    {
        "code": "L1007260389",
        "iid": 297204,
        "id": "61c837b53ea13c74b9141a40",
        "name": "Hoàng Công Sáng",
        "user_organizations": 2172939,
        "roles": 2,
    },
    {
        "code": "L1009060431",
        "iid": 297172,
        "id": "61c837b13ea13c74b9141a20",
        "name": "Vũ Thị Kim Toàn",
        "user_organizations": 2172936,
        "roles": 2,
    },
    {
        "code": "L1009060375",
        "iid": 297131,
        "id": "61c837ab3ea13c74b91419f7",
        "name": "Lưu Văn Việt",
        "user_organizations": 2172935,
        "roles": 2,
    },
]
school = lms.New(dmn="bvl", debug=True)
name_role_target = "Tạo khoá học"


def get_name_role(name_role):
    pattern = r"\((.*?)\)"
    matches = re.findall(pattern, name_role)
    return matches[0].lower()


for i in data:
    iid_user = i["iid"]
    iid_org = i["user_organizations"]
    # Nếu chưa là giảng viên thì cấp quyền giảng viên
    if i["roles"] == 1:
        handler_staff_of_user(school, iid_user=iid_user, iid_org=iid_org, status="add")

    # Tìm quyền đang có
    idd_roles = []
    role_applied_of_user = get_role_applied_of_user(school, iid_user, iid_org)
    for r in role_applied_of_user:
        idd_roles.append(r["iid"])

    # thêm quyền mới
    role_can_apply_for_user = get_role_can_apply_for_user(
        school, iid_user=i["iid"], iid_org=i["user_organizations"]
    )
    for r in role_can_apply_for_user:
        if get_name_role(r["label"]) == name_role_target.lower():
            idd_roles.append(r["value"])
    update_role_for_user(
        school,
        iid_user=i["iid"],
        iid_applied_target=i["user_organizations"],
        idd_roles=set(idd_roles),
    )
