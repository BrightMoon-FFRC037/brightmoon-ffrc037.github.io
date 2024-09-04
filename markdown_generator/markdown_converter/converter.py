yaml_front_matter = r'''---
title: ""
excerpt: ""
collection: 
category: 
---


'''
#modify relative path for different files to process
path = r''


with open(path, 'r') as file:
    content = file.read()
    count = 0
    i = 0
    while i <= len(content)-1:
        if content[i] == '$':
            count = count + 1
            if i-1 >= 0 and i+1 <= len(content)-1: #to exclude to beginner and ender
                if count % 2 == 1 and (content[i-1] != '$' and content[i+1] != '$'):
                    content = content[:i]+r'\\('+content[i+1:]
                elif count % 2 == 0 and (content[i-1] != '$' and content[i+1] != '$'):
                    content = content[:i]+r'\\)'+content[i+1:]
            elif i == 0:
                if content[i+1] != '$':
                    content = r'\\('+content[1:]
            elif i == len(content)-1:
                if content[i-1] != '$':
                    content = content[:i]+r'\\)'
        i = i + 1
with open(path, 'w') as file:
    content = yaml_front_matter + content
    file.write(content)    
