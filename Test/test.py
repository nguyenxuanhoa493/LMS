a = {
    "success": True,
    "message": "Thành công",
    "is_guest": False,
    "objects": {"count": 0, "total": 0},
    "hasSystemMessage": False,
    "ts": "",
    "server_ts": 1704729432,
}
import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API.until import get_value

print(get_value(input_data=a, key="result", default=[]))
