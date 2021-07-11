# WiFi账号密码
WIFI_SSID = "xxx"
WIFI_PASSWORD = "xx"

# 网站账号密码
USER = "xxx"
PWD = "xxx"

# 登录连接
LoginURL = "xxx"

# 数据回流地址
""" 
get 获取接口数据
post 提交本机数据
""" 
DataURL = "xxx"

# 请求头
HEADERS = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

try:
    from product_config import *
except Exception as e:
    pass