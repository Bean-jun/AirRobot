# -*- encoding:utf-8 -*-
import json
from utils.connect import connect
from utils.sleep import sleep
from utils.show_chinese import show
from utils.show_text import GUI
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

                article = response["msg"]["文章数量"]
                count = response["msg"]["访问数量"]
                temp = response["msg"]["天气情况"]["temperature"]
                aqi = response["msg"]["天气情况"]["aqi"]
                ip = response["msg"]["访问记录"][0][0]

                data = json.dumps(response)
                response = data.encode().decode()
                print(response)
        except Exception as e:
            print(e.args)
            # 失败重新登录即可
            token = login()

        try:
            data = "article:{},count:{},temp:{},aqi:{},ip:{}".format(article,count, temp, aqi, ip)
            data = data.split(',')
            print(data)
        except Exception as e:
            print(e.args)
            data = "faild"
        
        i = 0
        GUI.fill(0)
        for d in data:
            GUI.text(d,0,i*10)
            i += 1
        GUI.show()

        # 4、上传数据
        res, status = system(token)
        if status is True:
            print("上传成功")
            GUI.text("uploads success",0,50)
        else:
            print("上传失败")
            GUI.text("uploads faild",0,50)
            
        GUI.show()
            
        sleep(6)

if __name__ == "__main__":
    main()