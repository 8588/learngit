# import re
# r=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
# print(r)

# r=re.split(r'\s+','a b  c')
# print(r)

# r=re.split(r'[\s\,]+','a,b,c d   e')
# print(r)

# r=re.split(r'[\s\,\;]+','a,b;c d   e')
# print(r)

# r=re.match(r'^(\d{3})\-(\d{3,8})$','010-12345')
# print(r)
# print(r.group(0))
# print(r.group(1))
# print(r.group(2))



# # 多进程(Linux)
# import os

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



# # 多进程(跨平台)
# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# # Pool
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     start = time.time()
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(10):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % ('TOTAL', (end - start)))

# # 子进程
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# # 子进程输入
# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# # 进程间通讯
# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()


# # 多线程
# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# # lock
# import time, threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# # 死循环
# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()


# # ThreadLocal
# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()

# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# import os
# import time
# from datetime import datetime, timedelta

# print(datetime.fromtimestamp(1505178597))

# import itertools
# natuals = itertools.count(1)
# for n in natuals:
# 	print(n)


# cs = itertools.cycle('abc')
# for n in cs:
# 	print(n)



# ns = itertools.repeat('ABC',3)
# for n in ns:
# 	print(n)

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x:x<=10, natuals)
# print(list(ns))

# for c in itertools.chain('ABC', 'XYZ', '123'):
# 	print(c)

# for key, group in itertools.groupby('AAABBBCCAAA陈陈'):
# 	print(key, list(group))

# contextlib
# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)


# with Query('Bob') as q:
#     q.query()


# from contextlib import contextmanager

# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def query(self):
#         print('Query info about %s...' % self.name)

# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')


# with create_query('Bob') as q:
#     q.query()

# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)

# with tag("h1"):
#     print("hello")
#     print("world")

# from contextlib import closing
# from urllib.request import urlopen

# with closing(urlopen('http://10.26.0.244:8080/log/abc')) as page:
#     for line in page:
#         print(line)

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

#     def end_element(self, name):
#         print('sax:end_element: %s' % name)

#     def char_data(self, text):
#         print('sax:char_data: %s' % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# HTMLParser
# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

from urllib import request, parse

print('Login to http://10.26.203.10:8030/...')
login_data = parse.urlencode([
    ('tbUser', 'IFSEXP'),
    ('tbPwd', 'ifsexp'),
    ('pagerefer', 'http://10.26.203.10:8030/Login.aspx'),
    ('__VIEWSTATE', 'XlbIAIlXM63vxaVVTRaGaOJxLw5T9eZ45kaSFT8cnSbNawJ0O/4f9qPI1xLklM8b8yUSda4yhHALj6C3lKvw2LRKbJYJIszS7ByKlhhpxZU='),
    ('__EVENTVALIDATION','mNV42aXY/L9L9jb97kjbEQFr17aSu8LQ4/UkuNHdhJ/dC+2mjWDvvVNkL8drsoj+R20dxrYR3bnaMa3S+PKFtGWaFkwWY+x9hVY/p31u/s3pxKUczP30C9XxJMJaZRWET1IG1iJxxTdQGwFRE3YMTFJIVkOn6nh8VnRRezMmEYI=')
])

req = request.Request('http://10.26.203.10:8030/')
req.add_header('Origin', 'http://10.26.203.10:8030/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:55.0) Gecko/20100101 Firefox/55.0')
req.add_header('Referer', 'http://10.26.203.10:8030/Login.aspx')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_header('Cookie', 'ASP.NET_SessionId=4sfo3xtorkrm0wrwhezu0kpr')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))