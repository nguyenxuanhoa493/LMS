import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms, certificate

school = lms.New(dmn="xanhsm")


list_cer = [
    {"name": "Kỹ năng tư duy tích cực và sáng tạo", "code": "KNM01"},
    {"name": "Giải quyết vấn đề một cách logic", "code": "KNM02"},
    {"name": "Bí quyết tăng doanh số thông qua dịch vụ khách hàng", "code": "KNM03"},
    {"name": "Phương pháp huấn luyện nhân viên hiệu quả", "code": "KNM04"},
    {"name": "Sử dụng trí tuệ cảm xúc trong công việc", "code": "KNM05"},
    {"name": "Phương pháp tạo động lực làm việc cho nhân viên", "code": "KNM06"},
    {"name": "Kỹ năng quản lý và giải quyết xung đột", "code": "KNM07"},
    {"name": "Sử dụng trí tuệ cảm xúc trong công việc", "code": "KNM08"},
    {"name": "Kỹ năng ủy thác công việc", "code": "KNM09"},
    {"name": "Kỹ năng giao tiếp", "code": "KNM10"},
    {"name": "5 tư duy cần có thời 4.0", "code": "KNM11"},
]
id_cer_template = "657fee7f4b38ccad79086e53"

for cer in list_cer:
    certificate.new(
        school,
        name_cer=cer["name"],
        code_cer=cer["code"],
        id_cer_template=id_cer_template,
    )
