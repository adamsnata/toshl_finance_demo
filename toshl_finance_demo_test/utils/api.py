from datetime import datetime

import allure
from requests import Session

from config import config
from toshl_finance_demo_test.data.transaction import EntryType
from toshl_finance_demo_test.utils.api_utils import reqres_session


def add_entry(session: Session, entry_type: EntryType, category_id: str, amount: int, tag_ids=None):
    if entry_type == EntryType.EXPENSE:
        amount = -amount

    if tag_ids is None:
        tag_ids = []
    else:
        tag_ids = [','.join(tag_ids)]
    with allure.step("Add expense with API"):
        reqres_session.post(url=f'/api/entries',
                     params={"immediate_update": "true"},
                     json={"amount": amount,
                           "date": datetime.now().strftime("%Y-%m-%d"),
                           "currency":
                               {"code": "GEL"
                                },
                           "account": "4346873",
                           "category": category_id,
                           "tags": tag_ids})


def get_all_entries():
    resp = reqres_session.get(url=f'/api/entries/',
                       params={"from": "2024-01-01", "to": datetime.now().strftime("%Y-%m-%d")})
    return resp.json()
