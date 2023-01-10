import itertools
import logging
import re
from typing import Optional

from db import forms

logger = logging.getLogger(__name__)

# data = [
#     { #"name": "Form 1",
#      "lead_email": "aaa@mail.ru",
#      "phone_number": "+7 952 259 99 44",
# #     "order_date": "2022-12-31",
#      "description": "Описание формы 1"},
#     {"name": "Form 2",
#      "lead_email": "bbb@mail.ru",
#      "phone_number": "+7 952 259 99 45",
#      "order_date": "2022-11-30",
#      "description": "Описание формы 2"},
#     {"name": "Form 3",
#      "lead_email": "ccc@mail.ru",
#      "phone_number": "+7 952 259 99 46",
#      "order_date": "2022-10-15",
#      "description": "Описание формы 3"},
#     {"name": "Form 4",
#      "lead_email": "ddd@mail.ru",
#      "phone_number": "+7 952 259 99 47"},
#     {"lead_email": "eee@mail.ru",
#      "phone_number": "+7 952 259 99 48",
#      "description": "Описание формы 5"},
#
# ]


data_to_bd = [
    {
        "name": "Form 1",
        "lead_email": "email",
        "phone_number": "phone",
        "order_date": "date",
        "description": "text"
    },
    {
        "name": "Form 2",
        "user_number": "phone",
        "date_of_birth": "date",
        "user_name": "text"
    },
    {
        "name": "Form 3",
        "shop_email": "email",
        "shop_info": "text"
    },
    {
        "name": "Form 4",
        "boss_email": "email",
        "boss_phone": "phone"
    },
    {
        "name": "Form 5",
    },
]

async def get_from_db(conditions) -> Optional[dict]:
    keys = list(conditions.keys())
    all_conditions = await sub_lists(keys)
    logger.info(all_conditions)

    for key in reversed(all_conditions):
        condition = {k: v for k, v in conditions.items() for i in key if k == i}
        logger.info(condition)
        db_record = forms.find_one(condition)

        if db_record:
            logger.info(key)
            logger.info(db_record)
            return {k: v for k, v in db_record.items() if v is not None}

    return None


async def sub_lists(my_list) -> list:
    subs = []
    for i in range(1, len(my_list) + 1):
        temp = [list(x) for x in itertools.combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)

    return subs


async def check_result(db_record, conditions) -> bool:
    copy = db_record.copy()
    copy.pop('_id')
    copy.pop('name')
    logger.info(copy)
    logger.info(conditions)
    for k, v in copy.items():
        if k in conditions.keys() and v != conditions.get(k) or k not in conditions.keys():
            return False

    return True


async def types_of_fields(d: str):
    types = {'email': r'^\S+@\w+.\w{2,4}$',
             'date': r'^[0-9]{2}[.][0-9]{2}[.][0-9]{4}$',
             'date_2': r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$',
             'phone': r'^[+][0-9][ ][0-9]{3}[ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}$'
             }
    for t, r in types.items():
        if re.fullmatch(r, d):
            if t == 'date_2':
                return 'date'

            return t

    return 'text'


async def type_form(data: dict):
    result = {}
    for k, v in data.items():
        result[k] = await types_of_fields(v)

    return result
