#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Drink:
    def __init__(self, name, price):
        self.quantity = 0
        self.name = name
        self.price = price
        
    def add_quantity(self):
        self.quantity += 1
        print("%s의 수량이 1 늘었습니다"% self.name)
        
    def sub_quantity(self):
        self.quantity -= 1
        print("%s의 수량이 1 줄었습니다"% self.name)
    

        