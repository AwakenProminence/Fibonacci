#!/usr/bin/python
#verson:python 3.5
#program to calculate fibinacci
#author:awaken


def fibo(n):
	a,b=0,1
	while a<n:
		print (a)
		a,b=b,a+b

n=int(input('Enter an integer: '))
fibo(n)

