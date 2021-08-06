"""
数据流显示
"""

import urequests
from config import DataURL, HEADERS



def display(token):
    """数据获取显示"""
    if token is None:
        return 

    try:
        url = DataURL + "?token=" + token
        response = urequests.get(url=url, headers=HEADERS)
        if response.status_code == 200:
            res = response.json()
            return res
    except Exception as e:
        return 