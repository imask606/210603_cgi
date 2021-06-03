#!/usr/bin/python3
#_*_ coding: utf-8 _*_
import cgi
import sys

form = cgi.FieldStorage()

print ("Content-Type: text/html; charset=utf-8\r\n")

if "text" not in form:
    print("<h1>あれ？</h1>")
    print("<br>")
    print("<a href='/'><button　type='submit'>戻る</button></a>")
    sys.exit()

text = form.getvalue("text")
print(text)