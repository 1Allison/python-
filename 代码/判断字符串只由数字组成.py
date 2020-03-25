def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def is_numeric(s):
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False

chri = input('请输入一段字符串')
#检测字符串是否只由数字组成
print(is_number(chri))
#检测字符串是否只由数字组成，这种方法是只针对unicode对象
print(is_numeric(chri))
