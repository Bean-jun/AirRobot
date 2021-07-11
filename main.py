# -*- encoding:utf-8 -*-
import json
from utils.connect import connect
from utils.sleep import sleep
from account.login import login
from steam.display import display
from steam.system import system



def main():
    """主线程"""

    # 1、连接网络
    msg = connect()
    if msg['status'] is False:
        print("连接失败")
        return 

    # 2、用户登录
    token = login()
    if token is None:
        print("登录失败")
        return
    
    while True:
        # 3、获取数据
        response = display(token)

        try:
            if response['status'] is not False:
                print("\n下载数据:")
                data = json.dumps(response)
                response = data.encode().decode()
                print(response)
        except Exception as e:
            print(e.args)
            # 失败重新登录即可
            token = login()

        # 4、上传数据
        status = system(token)
        if status is True:
            print("上传成功")
        else:
            print("上传失败")
            
        sleep(6)

if __name__ == "__main__":
    main()