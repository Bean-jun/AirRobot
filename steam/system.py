"""
系统数据流回传
"""

import os
import sys
import urequests
from config import DataURL, HEADERS



def system(token):
    """数据发送"""
    if token is None:
        return 

    data = {
        "name": os.uname()[0],
        "platform": sys.platform,
        "version": sys.version
    }

    try:
        url = DataURL + "?token=" + token
        response = urequests.post(url=url, json=data, headers=HEADERS)
        if response.status_code == 200:
            res = response.json()
            return res['status']
    except Exception as e:
        return False