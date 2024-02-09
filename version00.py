print("***********************************")
print("\t\t\t\t用户注册\n用户名规则：只能是大小写字母或者数字，不能以数字开头，长度为5~12位")
print("密码规则：密码必须且只能由大小写字母和数字组成，长度与为6~15位")
print("***********************************")

def ver_name(name):
    if 5 <= len(name) <=12 and ('A' <= name[0] <= 'Z' or 'a' <= name[0] <= 'z'):
        for i in range(1,len(name)):
            if '0' <= name[i] <= '9' or 'A' <= name[i] <= 'Z' or 'a' <= name[i] <= 'z':
                i += 1
                if i == len(name):
                    return 0
            else:
                return 1
    else:
        return 1

def ver_pw(pw1,pw2):
    if pw1 == pw2 and 6 <= len(pw1) <= 15:
        for i in range(0,len(pw1)):
            if '0' <= pw1[i] <= '9' or 'A' <= pw1[i] <= 'Z' or 'a' <= pw1[i] <= 'z':
                i += 1
                if i == len(pw1):
                    return 0
            else:
                return 1
    else:
        return 1


def ver_phone(phone):
    if phone[0] == '1' and len(phone) == 11:
        return 0
    else:
        return 1

count = 1
user = []
data = {'user_name':'','password':'','phone_number':''}
while 1 == 1:
    name = input("用户名：")
    pw1 = input('密码：')
    pw2 = input('确定密码：')
    phone = input("手机号：")
    count+=1
    if count > 1:
        if ver_name(name):
            print("\033[31m请输入有效用户名\033[0m")
        elif ver_pw(pw1, pw2) == 1:
            print("\033[31m密码输入不符合规则或两次输入不一致，请重新输入\033[0m")
        elif ver_phone(phone) == 1:
            print("\033[31m请输入有效手机号\033[0m")
        else:
            data['user_name'] = name
            data['password'] = pw1
            data['phone_number'] = phone
            user.append(data)
            print("\033[34m注册成功！\033[0m")
            break