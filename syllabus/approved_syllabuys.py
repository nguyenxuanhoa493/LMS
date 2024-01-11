import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.syllabus import approved

list_syllabus = [
    {"iid": 13276700, "id": "659ab516a36e55a687011c3b", "name": "M03_Tư duy hiệu quả"},
    {
        "iid": 13276653,
        "id": "659ab4f313476e03770b95f8",
        "name": "M02_Công việc của CVVH",
    },
    {
        "iid": 13276599,
        "id": "659ab3312dbb62c11109e0bf",
        "name": "M01_Tổng quan vận hành Taxi",
    },
    {
        "iid": 13273185,
        "id": "6599d91d09b9b6019a0ddc70",
        "name": "HƯỚNG DẪN CÁCH THỨC THU THẬP VÀ LƯU TRỮ CHỨNG CỨ_DÀNH CHO LỚP MỚI",
    },
    {"iid": 13268184, "id": "659924c17656fec100030171", "name": "Bác Tài Xanh"},
    {"iid": 13268153, "id": "6599222fa57f31fe9e03bdd2", "name": "Kiểm Tra Cuối Khóa"},
    {
        "iid": 13267598,
        "id": "65991b5b56468990c406ce58",
        "name": "TẬP HUẤN NGHIỆP VỤ VẬN TẢI DÀNH CHO LÁI XE VÀ NHÂN VIÊN PHỤC VỤ XE",
    },
    {
        "iid": 13266864,
        "id": "6598f6a0a5e8faa9790f9a0b",
        "name": "Hướng dẫn sử dụng Vivi",
    },
    {
        "iid": 13266769,
        "id": "6598ef59478860f5e606536b",
        "name": "HCM_Hướng dẫn vận doanh sân bay dành cho TXTX",
    },
    {"iid": 13253530, "id": "65968299d0f5d8b3860738ca", "name": "Bác Tài Xanh"},
    {"iid": 13245645, "id": "65950aea5f3e19da0f0e1f8a", "name": "M07"},
    {
        "iid": 13242046,
        "id": "65949b667a0493b2ef05ef29",
        "name": "M06-Quy trình và hướng dẫn thực hiện công việc dành cho Tài xế Xanh SM",
    },
    {
        "iid": 13242010,
        "id": "659499e62f285234a90e9cca",
        "name": "M05-App dành cho Tài xế",
    },
    {
        "iid": 13241954,
        "id": "659493c00911fc34800fdc9c",
        "name": "M04-Kiến thức sản phẩm",
    },
    {
        "iid": 13241943,
        "id": "659491e8b9c0eb2ba502c433",
        "name": "M03 - 7 Hành vi Dịch vụ",
    },
    {
        "iid": 13234253,
        "id": "6593a96e4d4027fe1c061614",
        "name": "M02_Tiêu chuẩn Dịch vụ",
    },
    {
        "iid": 13233707,
        "id": "659386b6970049f5710b1c3a",
        "name": "M01_Chào mừng gia nhập Hành trình Di chuyển xanh",
    },
    {
        "iid": 13229101,
        "id": "6592c0e849764ff1a7022e78",
        "name": "CVVH_Công việc của CVVH",
    },
    {
        "iid": 13229041,
        "id": "6592beff7a39a2098a0f84c9",
        "name": "CVVH_Tổng quan về Vận hành taxi",
    },
    {
        "iid": 13220858,
        "id": "658fea94d561da9e1e0154f9",
        "name": "Đào tạo Offline dành cho Tân binh",
    },
    {
        "iid": 13211552,
        "id": "658df95b04301cf396096ada",
        "name": "Chào mừng gia nhập Hành trình Di chuyển xanh",
    },
    {"iid": 13197190, "id": "658bcc88d878365ac9024984", "name": "môn demo 1"},
    {
        "iid": 13071470,
        "id": "657ff8df998946608701d1b3",
        "name": "Kỹ năng tư duy tích cực và sáng tạo",
    },
    {
        "iid": 13071456,
        "id": "657ff8dece72530ada062692",
        "name": "Giải quyết vấn đề một cách logic",
    },
    {
        "iid": 13071441,
        "id": "657ff8dea1b17a28230bfa4a",
        "name": "Bí quyết tăng doanh số thông qua dịch vụ khách hàng",
    },
    {
        "iid": 13071406,
        "id": "657ff8dd3c18ef33510ccf7e",
        "name": "Phương pháp huấn luyện nhân viên hiệu quả",
    },
    {
        "iid": 13071424,
        "id": "657ff8dd146b4d232801b028",
        "name": "Sử dụng trí tuệ cảm xúc trong công việc",
    },
    {
        "iid": 13071385,
        "id": "657ff8dc0906d1f53c0a74b7",
        "name": "Phương pháp tạo động lực làm việc cho nhân viên",
    },
    {
        "iid": 13071362,
        "id": "657ff8dba45cfb82fa0c6218",
        "name": "Kỹ năng quản lý và giải quyết xung đột",
    },
    {
        "iid": 13071343,
        "id": "657ff8da3be5a3decf01700a",
        "name": "Sử dụng trí tuệ cảm xúc trong công việc",
    },
    {
        "iid": 13071317,
        "id": "657ff8d9cfd605db6a065056",
        "name": "Kỹ năng ủy thác công việc",
    },
    {"iid": 13071303, "id": "657ff8d9c1397a75fb0c3c8f", "name": "Kỹ năng giao tiếp"},
    {
        "iid": 13071283,
        "id": "657ff8d8f1d134478507be5b",
        "name": "5 tư duy cần có thời 4.0",
    },
    {"iid": 13070884, "id": "657ff2f3cfd605db6a064fad", "name": "Giới thiệu về Vieted"},
]

school = lms.New(dmn="xanhsm", user_code="gsm")

for s in list_syllabus:
    approved(school, id_syllabus=s["id"], status="queued")
    approved(school, id_syllabus=s["id"])
