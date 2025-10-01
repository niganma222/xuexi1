"""
input（提示信息） 默认接受类型为 字符串
"""
#eg：
print("请告诉我你是谁")
name =input()
print("我知道了，你是%s" % name)
#等同于下面
name =input("请告诉我你是谁?\n")
print("我知道了，你是%s" % name)


#输入数字类型
num =input("清说话：")
#数据转换
num=int(num)
print("en:" ,type(num))#en: <class 'str'>


#eg:
user_name=input("请输入你的姓名：")
user_type=input("请输入你的等级：")
print(f"您好：{user_name},您是尊贵的：{user_type}用户，欢迎您的光临")