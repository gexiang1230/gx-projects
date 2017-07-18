# coding=utf-8 #
file1_path='C:\学习\python test\cfiles\cfiles\gbk编码.txt'#要读取的文件的路径
file2_path='C:\学习\python test\cfiles\cfiles\utf8编码.txt'

file_path1=unicode(file1_path,"utf-8")  # 读取的文件中
file_path2=unicode(file2_path,"utf-8")

with open(file_path1) as  f1, open(file_path2) as f2  :                                #打开文件1，文件2
    content1=f1.read().decode("gbk") #根据文件编码格式对文件进行解码
    content2 = f2.read().decode("utf8")
    newcontent=content1+'\t'+content2
    print newcontent       #str=g.decode('gbk').encode('utf-8')   #以gbk编码格式读取g（因为他就是gbk编码的）并转换为utf-8格式输出

    print u'请输入文件的名称：' #加 u等价于 Unicode，防止中文乱码

    newfile=raw_input()

    # 用户输入的内容的编码方式，和代码的运行环境有关， 如果是dos命令行执行 得到的是gbk编码
    uNewFile = newfile.decode('utf8')

    #将内容读写进新的文件中
    with open(uNewFile,'w') as f3:
        f3.write(newcontent.encode('utf-8'))

