#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__='Chen8'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')


def testpackage():
	from PIL import Image
	im=Image.open('test.png')
	print(im.format, im.size, im.mode)
	im.thumbnail((200,100))
	im.save('thumb2.jpg',"JPEG")

def print_score(std):
	print('%s: %s' % (std['name'],std['score']))

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
		


# 继承和多态		
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

# dog=Dog()
# dog.run()
# cat=Cat()
# cat.run()
a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))


# # pickling
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))


# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# JSON
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
print(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
p=json.loads(json_str)
print(p)

if __name__ == '__main__':
	test()

	# testpackage()
	# print(sys.path)
	# std1={'name':'Micheal','score':88}
	# std2={'name':'Jacky','score':98}
	# print_score(std1)
	# print_score(std2)

	# part=Student('Bart Simpson', 59)
	# lisa=Student('Lisa Simpson', 96)
	# part.print_score()
	# lisa.print_score()


from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

import uuid
print(uuid.uuid1())
print(uuid.uuid1())
