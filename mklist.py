#!/usr/bin/env python
import os
import csv
import collections
from datetime import datetime

def get_members(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        members = []
        for row in reader:
            members.append({
            'id' : row[0],
            'year':int(row[0].split('-')[0]),
            'num':int(row[0].split('-')[1]),
            'name_k': row[1],
            'name_f': row[2],
            'department': row[3]
            })
        mambers = sorted(members,key=lambda x: x['id'])
    return members

def get_departments(members):
    departments = set()
    for member in members:
        departments.add(member['department'])
    return list(departments)

def get_departments_members(members):
    departments_members = {}
    for department in get_departments(members):
        departments_members[department] = []
        for member in members:
            if(member['department'] == department ):
                departments_members[department].append(member)
    return departments_members

def get_output_dict(d_members):
    output_dict = {}
    for department in d_members.keys():
        output_dict[department] = {}
        year = datetime.now().strftime("%Y")
        output_dict[department]['h2']='<h2>'+str(year)+'年度入団 '+department+'</h2>\n'
        output_dict[department]['item']=[]
        for member in d_members[department]:
            image_path = os.path.join('data','images',member['id']+'.jpg')
            output_dict[department]['item'].append(
            '<article class="item">'+
                '<img src="'+ image_path +'" alt="member_image" class="image">'+
                '<p class="id">'+ member['id'] +'</p>'+
                '<p class="name_f">'+ member['name_f'] +'</p>'+
                '<p class="name_k">'+ member['name_k'] +'</p>'+
            '</article>')
    return output_dict

def get_line(items):
    lines = []
    for i in range((len(items)+4)//5):
        lines.append('<article class="line">')
        for j in range(5):
            index = i*5 + j
            if index < len(items):
                lines[i]+= items[index]
            else:
                lines[i] += '<article class="item"></article>'
        lines[i]+='</article>'
    return lines

def get_containers(lines):
    containers = []
    for i in range((len(lines)+3)//4):
        containers.append('<article class="container">')
        for j in range(4):
            index = i*4 + j
            if index < len(lines):
                containers[i] += lines[index]
            else: break
        containers[i] += '</article>'
    return containers

def get_pages(output_dict):
    pages = []
    for d_items in output_dict.items():
        print(d_items)
        items = d_items[1]
        h2 = items['h2']
        containers = get_containers(get_line(items['item']))
        for i in range(len(containers)):
            pages.append('<section class="page">'+h2+containers[i]+'</section>')
    return pages


def get_output_txt(output_dict):
    output = '''
<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>写真付き名簿</title>

</head>

<body>
'''
    pages = get_pages(output_dict)
    for page in pages:
        output+=page
    output+='</body></html>'
    return output

def write_index_html(output):
    pwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(pwd,'index.html')
    with open(path, 'w') as file:
        file.write(output)

if __name__ == '__main__':
    pwd = os.path.dirname(os.path.abspath(__file__))
    members = get_members(os.path.join(pwd,'data','csv','member_list.csv'))
    departments_members = get_departments_members(members)
    output_dict = get_output_dict(departments_members)
    output = get_output_txt(output_dict)
    write_index_html(output)
    print('SUCCESS!')
