from function import *

# 文件读取函数
def file_read():
    global content
    user_list = []
    line_list = content.split('\n')
    if len(line_list) > 2:
        for i in range(1, len(line_list)-1):
            line = line_list[i].strip(' ')

            username = line.split(',')[0]
            password = line.split(',')[1]
            phone = line.split(',')[2]

            user_dict = {}
            user_dict['username'] = username
            user_dict['password'] = password
            user_dict['phone'] = phone

            user_list.append(user_dict)
    else:
        return None

    return user_list


# 用户名输入函数
def input_name():
    name = input("用户名：")
    # temp = []
    # temp.append(name)
    user_list = file_read()

    if ver_name(name) == False:
        print("\033[31m用户名错误\033[0m")
        input_name()

    # for i in range(0,len(temp)-1):
    #    if name == temp[i]:
    #        print("\033[31m用户名已存在\033[0m")
    #        input_name()

    if user_list != None:
        for i in range(0,len(user_list)):
            dict = user_list[i]
            if name == dict['username']:
                print("\033[31m用户名已存在\033[0m")
                input_name()

    return name


# 密码输入函数
def input_password():
    pw1 = input("密码：")
    pw2 = input("确认密码：")
    if pw1 != pw2:
        print("\033[31m两次输入不一致\033[0m")
        input_password()

    if ver_password(pw1) == False:
        print("\033[31m密码错误\033[0m")
        input_password()

    return pw1


# 手机号输入函数
def input_phone():
    phone = input("手机号码：")
    if ver_phone(phone) == False:
        print("\033[31m手机号码错误\033[0m")
        input_phone()

    return phone


# 注册函数
def do_regi(name,password,phone):
    f = open('./temp.csv',mode='a+')
    # user = []
    # data = {'user_name':name,'password':password,'phone':phone}
    # user.append(data)
    f.write("%s,%s,%s\n" %(name,password,phone))
    f.close()
    return 1


def menu():
    i = input("继续注册：(y/n?)：")
    if i == 'y':
        return True
    elif i == 'n':
        return False

    menu()


if __name__ == '__main__':
    print("\033[32m*******************************************************\033[0m")
    print("\033[32m\t\t\t\t\t用户注册\n用户名规则：只能是大小写字母或者数字，不能以数字开头，长度为5~12位\033[0m")
    print("\033[32m密码规则：密码必须且只能由大小写字母和数字组成，长度与为6~15位\033[0m")
    print("\033[32m*******************************************************\033[0m")

    while menu() == True:
        file = open('./temp.csv')
        content = file.read()
        name = input_name()
        password = input_password()
        phone = input_phone()

        if do_regi(name,password,phone) == 1:
            print("\033[34m注册成功！\033[0m")
            file.close()