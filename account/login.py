"""
用户登录模块，获取token
"""

from utils import urequests
from config import LoginURL, USER, PWD, HEADERS


def login():
    """获取用户token"""
 
    data = {
        "email": USER,
        "password": PWD
        } 

    response = urequests.post(LoginURL, json=data, headers=HEADERS)
    if response.status_code == 200:
        try:
            res = response.json()
            token = res.get('token')
        except Exception as e:
            print(e.args)
            
    if token is not None:
        return token
    else:
        return