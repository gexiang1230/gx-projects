#coding=utf-8#
import requests
import csv
url='https://api.github.com/repos/unityka/myfile/issues'
#bug_name=raw_input('输入文件的名字:')
bug_name=r'C:\bug\bug.csv'
r=requests.get(url)
response_dicts=r.json()
with open(bug_name,'wb') as f:
    writer=csv.writer(f)
    writer.writerow(['标题','日期']) # 直接写表头 文件对象.writerow
    for repo_dict in response_dicts:
        save_file = []
        save_file.append(repo_dict['title'].encode('utf-8'))
        save_file.append(repo_dict['created_at'])
        writer.writerow(save_file)




















