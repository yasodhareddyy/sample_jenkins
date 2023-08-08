"""
1. Write a Python program to extract year, month and date from an url.
 "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

"""
import re
import datetime

s="https://www.washingtonpost.com/news/football-insider/wp/2016/september/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
date=r"(\d{4})/(\w+)/(\d{2})"
res=re.search(date,s)
d=res.group()
print(d)
#x=datetime.

#print(f"Year : {res.group(1)} \nMonth : {res.group(2)} \nDate : {res.group(3)}")
