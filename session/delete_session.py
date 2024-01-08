import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.session import delete_session

list_session = [
    "65976456e9350799b40ace6b",
    "658a7c6adebe8bc5c30517d4",
    "6583e8326f41798d6f0dd700",
    "65769ecccb93a2c50d0c4405",
    "657293429c8ac50d9903f03a",
    "65703e6138f29c06470ac201",
    "656fe0819f8c9b6309032885",
    "6569b0b650ae84033b099d9a",
    "656940d6e93ee8b21303a9d1",
    "6567ea72efba241727075239",
    "656806652929a746210d4f34",
    "65654a3df58d07f51507043b",
    "65519e1e8ca8f068670f2f89",
    "655031888a4b0461c80d51a5",
    "6549f98c55bd86277c4d9095",
    "654058cceb84fc1d9b00f83e",
    "653a2fba31662110245e7898",
    "6523d23249268165f4024817",
    "651eaa976b3e300a480ee9e6",
    "64feb28af1c0976fad271397",
    "64f99449ae9ee334b71e1c8d",
    "64eef2048355b326497dcaa7",
    "64eebe834aafeb1b8710ae44",
    "654a082510f0b374042f747e",
]

school = lms.New(dmn="meet")
for i in list_session:
    delete_session(school, id_session=i)
