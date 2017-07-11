# -*-coding:UTF-8 -*-
import re,pprint
def putInfoToDict(fileName):
   afterstr = {}
   with open(file) as data_file:
     inifile=data_file.read().splitlines()
     for line in inifile:
         inifile2=re.split(",|\n|\)|\(",line)       #对每行的每个元素进行切割
         new_list = [x for x in inifile2 if x != '']#在新增的initfile2的列表中删除空格
         studentid=int(new_list[2])                                     # #使用字典(Dictionary) keys() 函数以列表返回一个字典所有的键。
         infostr = {'checktime':new_list[0],'lessionid':new_list[1]} #infostr['studentid']获取指定键的值
         afterstr.setdefault(studentid,[]).append(infostr)#先添加到字典中在输出，dict.setdefault(key, default=None)，获取相同Key的 value

   pprint.pprint(afterstr)                             #

file='C:\\pycharm-modle-test\\05homework.txt'
putInfoToDict(file)