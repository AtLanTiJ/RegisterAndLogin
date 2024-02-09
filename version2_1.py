from function import *
import os

# 用户名输入函数
def input_name():
    name = input("用户名：")
    user_list = file_read(path)

    if not ver_name(name):
        print("\033[31m用户名不符合规则\033[0m")
        input_name()

    if user_list is not None:
        for i in range(0, len(user_list)):
            user_dict = user_list[i]
            if name == user_dict['name']:
                print("\033[31m用户名已存在\033[0m")
                input_name()

    return name


# 密码输入函数
def input_password(flag):
    pw1 = input("密码：")

    if not ver_password(pw1):
        print("\033[31m密码不符合规则\033[0m")
        input_password(flag)

    if flag in {1, 3}:
        pw2 = input("确认密码：")
        if pw1 != pw2:
            print("\033[31m两次输入不一致\033[0m")
            input_password(flag)

    return pw1


# 手机号输入函数
def input_phone():
    phone = input("手机号码：")
    if not ver_phone(phone):
        print("\033[31m手机号码错误\033[0m")
        input_phone()

    return phone


# 注册函数
def do_regi(name=None):
    f = open(path, mode='a+')
    if name is None:
        name = input_name()
    else:
        print("在注册用户：%s" % name)
    password = input_password(1)
    phone = input_phone()
    f.write("%s,%s,%s\n" % (name, password, phone))
    print("\033[34m注册成功！\033[0m")
    f.close()
    menu(1)


# 登录函数
def do_login():
    name = input("用户名：")
    if not ver_name(name):
        print("\033[31m用户名不符合规则【0m")
        do_login()
    i = get_user(path, name)
    user_list = file_read(path)
    error = 0
    if i is not None:
        password = input_password(2)
        if user_list[i]['password'] == password:
            print("\033[34m登陆成功\033[0m")
            menu(2, temp=name)
        else:
            print("\33[31m密码错误\033[0m")
            error += 1
            if error >= 3:
                exit(0)
            else:
                do_login()
    _in = input("用户不存在,是否注册(y/n?):")
    if _in == 'y':
        do_regi(name=name)
    else:
        do_login()


# 修改密码函数
def do_change(path, name):
    print("请输入旧密码")
    password = input_password(2)
    user_list = file_read(path)
    i = get_user(path, name)

    if i is not None:
        if user_list[i]['password'] == password:
            print("请在下方输入新密码")
            newpass = input_password(3)
            user_list[i]['password'] = newpass
            with open(path, mode='w+') as f:
                key_list = []
                for k in user_list[0].keys():
                    key_list.append(k)
                    key = ','.join(key_list)
                f.write(f"{key}\n")
                for j in range(0, len(user_list)):
                    value_list = []
                    for v in user_list[j].values():
                        value_list.append(v)
                    value = ','.join(value_list)
                    f.write(f"{value}\n")
                menu(2)
        else:
            print("\033[31m密码错误\033[0m")
            do_change(path, name)
    else:
        print("\033[31m用户名错误\033[0m")
        do_change(path, name)


# 菜单函数
def menu(flag, temp=None):
    if flag == 1:
        print("\033[32m==========菜单==========\033[0m")
        print("\033[32m【1、注册   2、登录   3、退出】\033[0m")
        i = input("\033[32m请选择(1、2、3)：\033[0m")
        if i == '1':
            do_regi()
        elif i == '2':
            do_login()
        elif i == '3':
            exit(0)
        else:
            menu(flag)

    elif flag == 2:
        print("\033[32m==========用户菜单（%s）==========\033[0m" % temp)
        print("\033[32m【1、修改密码   2、返回   3、退出】\033[0m")
        i = input("\033[32m请选择(1、2、3)：\033[0m")
        if i == '1':
            do_change(path, temp)
        elif i == '2':
            menu(1)
        elif i == '3':
            exit(0)
        else:
            menu(flag)


if __name__ == '__main__':
    print("\033[32m*******************************************************\033[0m")
    print("\033[32m\t\t\t\t\t用户注册\n用户名规则：只能是大小写字母或者数字，不能以数字开头，长度为5~12位\033[0m")
    print("\033[32m密码规则：密码必须且只能由大小写字母和数字组成，长度与为6~15位\033[0m")
    print("\033[32m*******************************************************\033[0m")
    path = './temp.csv'
    menu(1)
