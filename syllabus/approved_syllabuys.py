import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.syllabus import approved

list_syllabus = [
    {"id": "6589bf6bfd383f88ac0fd150", "iid": 56988019, "name": "Địa lí 8"},
    {"id": "6589bf6bcbf250edbc0dbd42", "iid": 56988020, "name": "Địa lí 9"},
    {"id": "6589bf6b291543401600e880", "iid": 56988018, "name": "Địa lí 7"},
    {"id": "6589bf6acfdf4c82b10e3b89", "iid": 56988017, "name": "Địa lí 6"},
    {"id": "6589bf6a9da7ffc7de0f2faf", "iid": 56988014, "name": "Lịch sử 7"},
    {"id": "6589bf6a8bec5fe9f60c9b83", "iid": 56988016, "name": "Lịch sử 9"},
    {"id": "6589bf6a717b53effc0bff1f", "iid": 56988015, "name": "Lịch sử 8"},
    {"id": "6589bf69af94d129bc06150f", "iid": 56988010, "name": "Sinh học 7"},
    {"id": "6589bf697e3c043c5b0868e8", "iid": 56988012, "name": "Sinh học 9"},
    {"id": "6589bf6919dfbff4750b56a1", "iid": 56988013, "name": "Lịch sử 6"},
    {"id": "6589bf6916c0422ee5023b28", "iid": 56988011, "name": "Sinh học 8"},
    {"id": "6589bf681b0d6ddc630f07ff", "iid": 56988009, "name": "Sinh học 6"},
    {"id": "6589bf6819633214a00dde8d", "iid": 56988008, "name": "Hoá học 9"},
    {"id": "6589bf63cccf06ae1a0aca1f", "iid": 56988007, "name": "Hoá học 8"},
    {"id": "6589bf62d8af5ca8260980c2", "iid": 56988005, "name": "Vật lí 8"},
    {"id": "6589bf62c5278d44c00c844d", "iid": 56988003, "name": "Vật lí 6"},
    {"id": "6589bf625095b9cf010dd587", "iid": 56988006, "name": "Vật lí 9"},
    {"id": "6589bf6239cd6c34f80b7e00", "iid": 56988004, "name": "Vật lí 7"},
    {"id": "6589bf61cd8500cf1e03161b", "iid": 56987999, "name": "Công nghệ 6"},
    {"id": "6589bf6181df226cc10eb690", "iid": 56988002, "name": "Công nghệ 9"},
    {"id": "6589bf6162c08466b304d7dd", "iid": 56988000, "name": "Công nghệ 7"},
    {"id": "6589bf6161297d89920e83d2", "iid": 56988001, "name": "Công nghệ 8"},
    {"id": "6589bf609cb5cf53980c1aa0", "iid": 56987996, "name": "Giáo dục công dân 7"},
    {"id": "6589bf60867b4ce527072bfc", "iid": 56987995, "name": "Giáo dục công dân 6"},
    {"id": "6589bf606d0577e8170a4ec9", "iid": 56987997, "name": "Giáo dục công dân 8"},
    {"id": "6589bf602415ce838102e233", "iid": 56987998, "name": "Giáo dục công dân 9"},
    {
        "id": "6589bf5f4adabc4c000761ba",
        "iid": 56987992,
        "name": "Hoạt động trải nghiệm 7",
    },
    {
        "id": "6589bf5f1b4443a43404a577",
        "iid": 56987994,
        "name": "Hoạt động trải nghiệm 9",
    },
    {
        "id": "6589bf5f129b054fba013421",
        "iid": 56987991,
        "name": "Hoạt động trải nghiệm 6",
    },
    {
        "id": "6589bf5f0c1a0b54ce030b54",
        "iid": 56987993,
        "name": "Hoạt động trải nghiệm 8",
    },
    {"id": "6589bf5eba2d672bc60698b4", "iid": 56987990, "name": "Tiếng anh 9"},
    {"id": "6589bf5eb4f7cd02e40cd409", "iid": 56987987, "name": "Tiếng anh 6"},
    {"id": "6589bf5e32b7d19b990b7202", "iid": 56987988, "name": "Tiếng anh 7"},
    {"id": "6589bf5e1adead3cad0fe2f2", "iid": 56987989, "name": "Tiếng anh 8"},
    {"id": "6589bf5df5c14222ec0a78e4", "iid": 56987985, "name": "Giáo dục thể chất 8"},
    {"id": "6589bf5d4a7b2ffa39028d27", "iid": 56987984, "name": "Giáo dục thể chất 7"},
    {"id": "6589bf5d4210acd7b90f3654", "iid": 56987983, "name": "Giáo dục thể chất 6"},
    {"id": "6589bf5d13fe62900505850a", "iid": 56987986, "name": "Giáo dục thể chất 9"},
    {"id": "6589bf5cce272a617f0405b6", "iid": 56987981, "name": "Mĩ thuật 8"},
    {"id": "6589bf5c7248032fb2039256", "iid": 56987978, "name": "Âm nhạc 9"},
    {"id": "6589bf5c3eeb63144e02c9c1", "iid": 56987980, "name": "Mĩ thuật 7"},
    {"id": "6589bf5c3410e4085d04fa7e", "iid": 56987982, "name": "Mĩ thuật 9"},
    {"id": "6589bf5c25c56a7861063be1", "iid": 56987979, "name": "Mĩ thuật 6"},
    {"id": "6589bf5bc9a599a1b20061c2", "iid": 56987976, "name": "Âm nhạc 7"},
    {"id": "6589bf5bb3f80c63d2071c43", "iid": 56987975, "name": "Âm nhạc 6"},
    {"id": "6589bf5b6d18f6991b0ddc4f", "iid": 56987977, "name": "Âm nhạc 8"},
    {"id": "6589bf5af3561b8947003855", "iid": 56987972, "name": "Ngữ văn 7"},
    {"id": "6589bf5a94ef9b71930b9ab5", "iid": 56987973, "name": "Ngữ văn 8"},
    {"id": "6589bf5a319e4c4bed0b1d98", "iid": 56987974, "name": "Ngữ văn 9"},
    {"id": "6589bf59c21f751250048361", "iid": 56987970, "name": "Toán 9"},
    {"id": "6589bf59b3ffd9c75505a350", "iid": 56987969, "name": "Toán 8"},
    {"id": "6589bf596fa8b1534d0d9dd2", "iid": 56987971, "name": "Ngữ văn 6"},
    {"id": "6589bf58ef4c6d041b0bc63a", "iid": 56987968, "name": "Toán 7"},
    {"id": "6589bf5840f5254c5d0e12ad", "iid": 56987967, "name": "Toán 6"},
]

school = lms.New(dmn="ve", type_dmn="bgg")

for s in list_syllabus:
    approved(school, id_syllabus={s["id"]})
