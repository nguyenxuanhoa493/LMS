import sys
from random import randint
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.practice import update_practice_correct_count

school = lms.New(dmn="xanhsm")
list_user = [
    708226,
    707736,
    707735,
    707734,
    707733,
    707732,
    707731,
    707730,
    707729,
    707728,
    707727,
    707726,
    707725,
    707724,
    707723,
    707722,
    707721,
    707720,
    707719,
    707718,
    707717,
    707716,
    707715,
    707714,
    707713,
    707712,
    707711,
    707710,
    707709,
    707708,
    707707,
    707706,
    707705,
    707704,
    707499,
]

for u in list_user:
    update_practice_correct_count(
        school,
        iid_user=u,
        iid_sco=13103061,
        correct_count=randint(50, 550),
        created_ts=randint(1701428560, 1703070178),
    )
