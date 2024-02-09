import re


# 用户名规则：只能是大小写字母或者数字，不能以数字开头，长度为5~12位
def ver_name(name):
    if ord(name[0]) in range(48, 58):
        return False

    if not (len(name) in range(5, 12)):
        return False

    for content in name:
        if not (ord(content) in range(65, 91) or ord(content) in range(97, 123) or ord(content) in range(48, 58)):
            return False

    return True


# 密码规则：密码必须且只能由大小写字母和数字组成，长度与为6~15位
def ver_password(pw):
    if not (len(pw) in range(6, 15)):
        return False

    cap = 0
    num = 0
    min = 0
    other = 0
    for content in pw:
        if ord(content) in range(48, 58):
            num += 1
        elif ord(content) in range(97, 123):
            min += 1
        elif ord(content) in range(65, 91):
            cap += 1
        else:
            other += 1
    if 0 in (cap, num, min) or other != 0:
        return False

    return True


# 手机号规则：11位长度以1开头，第二位不能是0、1、2
def ver_phone(phone):
    if len(phone) != 11:
        return False

    if (phone[0] != '1') or (phone[1] in ('0', '1', '2')):
        return False

    for content in phone:
        if not (ord(content) in range(48, 58)):
            return False

    return True


# 读取CSV文件函数
def file_read(path, has_row=True):
    line_list = []
    with open(path) as f:
        line_list = f.readlines()

    key_list = line_list[0].strip().split(',')  # 取第一行的字符串切片作为字典键值

    user_list = []
    if has_row:
        for i in range(1, len(line_list)):
            temp_list = line_list[i].strip().split(',')

            user_dict = {}
            for j in range(len(key_list)):
                user_dict[key_list[j]] = temp_list[j]

            user_list.append(user_dict)

            if user_list == ['']:
                return None
    else:
        return None

    return user_list


# 用户查找函数
def get_user(path, username):
    user_list = file_read(path)
    for i in range(0, len(user_list)):
        if user_list[i]['name'] != username:
            i += 1
        else:
            return i

    return None


# 测试函数
def test(func, expect, *args):
    if func(*args) == expect:
        print("函数 %s 测试 %s：成功" % (func.__name__, *args))
    else:
        print("函数 %s 测试 %s：失败" % (func.__name__, *args))

# if __name__ == '__main__':
# # 对用户名规则函数测试
#     test(ver_name,False,'12345')
#     test(ver_name,False,'qwer')
#     test(ver_name,False,'iuuiooutyuiguhjksydiufhjk')
#     test(ver_name,False,'wert[')
#     test(ver_name,True,'qwert')
#     test(ver_name,True,'qwiiert')


# # 对密码规则函数测试
#     test(ver_password,False,'/.;uiojhksdfg')
#     test(ver_password,False,'12Ab5')
#     test(ver_password,False,'123456')
#     test(ver_password,False,'uiuiui')
#     test(ver_password,False,'AAAAAA')
#     test(ver_password,False,'ABhkuio')
#     test(ver_password,False,'ABh12iyuijkhjhhjkhjkhjkhjkhjkhjk')
#     test(ver_password,True,'ABcd123')


# # 对手机号规则函数测试
#     test(ver_phone,False,'10156789098')
#     test(ver_phone,False,'11156789098')
#     test(ver_phone,False,'12156789098')
#     test(ver_phone,True,'13156789098')
#     test(ver_phone,False,'131567890')
#     test(ver_phone,False,'131567890989')
#     test(ver_phone,False,'13156a89、989')
