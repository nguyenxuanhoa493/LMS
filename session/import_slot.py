import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms, slot

list_slot = [
    {"name": "Tiết 1", "start_time": 370, "end_time": 420},
    {"name": "Tiết 2", "start_time": 420, "end_time": 470},
    {"name": "Tiết 3", "start_time": 470, "end_time": 520},
    {"name": "Tiết 4", "start_time": 520, "end_time": 570},
    {"name": "Tiết 5", "start_time": 590, "end_time": 640},
    {"name": "Tiết 6", "start_time": 640, "end_time": 690},
    {"name": "Tiết 7", "start_time": 750, "end_time": 830},
    {"name": "Tiết 8", "start_time": 830, "end_time": 880},
    {"name": "Tiết 9", "start_time": 900, "end_time": 950},
    {"name": "Tiết 10", "start_time": 950, "end_time": 1000},
    {"name": "Tiết 11", "start_time": 1000, "end_time": 1050},
    {"name": "Tiết 12", "start_time": 1095, "end_time": 1145},
    {"name": "Tiết 13", "start_time": 1145, "end_time": 1195},
    {"name": "Tiết 14", "start_time": 1195, "end_time": 1245},
]
school = lms.New(dmn="ve", type_dmn="bgg")
for s in list_slot:
    print(s)
    slot.new(
        school, name_slot=s["name"], start_time=s["start_time"], end_time=s["end_time"]
    )
