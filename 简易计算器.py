from conkits import Conio
error=False
int_error=False
str_error=False
other_error=False
del_error=False

#存储器
memorizer={}

#输入和输出
while True:
    Conio.clrscr()
    print(memorizer)
    print('''
赋值语句：LET 单元名称,值
删除语句：DEL 单元名称
加法语句：ADD 值1,值2,单元名称
减法语句：SUB 值1,值2,单元名称
乘法语句：MUL 值1,值2,单元名称
除法语句：DIV 值1,值2,单元名称
转整语句：INT 单元名称
转字语句：STR 单元名称
''')
    if error==True:
        print('解析器无法解析！')
        print()
        error=False
    elif int_error==True:
        print('无法转换整形！')
        print()
        int_error=False
    elif str_error==True:
        print('无法转换字符串！')
        print()
        str_error=False
    elif other_error==True:
        print('语法不正确！')
        print()
        other_error=False
    elif del_error==True:
        print('无法删除单元！')
        print()
        del_error=False
    else:
        pass
    key=input('>>>')

#解析器
    try:
        if 'LET' in key:
            key=key.replace('LET','')
            key=key.strip()
            key=key.split(',')
            save=key[0]
            ver1=key[1]
            memorizer[save]=ver1
        elif 'INT' in key:
            key=key.replace('INT','')
            key=key.strip()
            try:
                ver1=int(memorizer[key])
                memorizer[key]=ver1
            except:
                int_error=True
        elif 'STR' in key:
            key=key.replace('STR','')
            key=key.strip()
            try:
                ver1=str(memorizer[key])
                memorizer[key]=ver1
            except:
                str_error=True
        elif 'ADD' in key:
            key=key.replace('ADD','')
            key=key.strip()
            key=key.split(',')
            ver1=key[0]
            ver2=key[1]
            save=key[2]
            memorizer[save]=memorizer[ver1]+memorizer[ver2]
        elif 'SUB' in key:
            key=key.replace('SUB','')
            key=key.strip()
            key=key.split(',')
            ver1=key[0]
            ver2=key[1]
            save=key[2]
            memorizer[save]=memorizer[ver1]-memorizer[ver2]
        elif 'DEL' in key:
            key=key.replace('DEL','')
            key=key.strip()
            try:
                del memorizer[key]
            except:
                del_error=True
        elif 'MUL' in key:
            key=key.replace('MUL','')
            key=key.strip()
            key=key.split(',')
            ver1=key[0]
            ver2=key[1]
            save=key[2]
            memorizer[save]=memorizer[ver1]*memorizer[ver2]
        elif 'DIV' in key:
            key=key.replace('DIV','')
            key=key.strip()
            key=key.split(',')
            ver1=key[0]
            ver2=key[1]
            save=key[2]
            memorizer[save]=memorizer[ver1]/memorizer[ver2]
        else:
            error=True
    except:
        other_error=True