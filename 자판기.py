#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from drink import Drink

select, money, balance = 0, 0, 0
cocofarm = Drink("cocofarm", 700)
coca_cola = Drink("coca_cola", 1000)
tomato_juice = Drink("tomato_juice", 300)
        
def service_customer(select):
    money = int(input("돈을 넣어주세요."))
    if select==1:
        if cocofarm.quantity>0:
            order(cocofarm, money)
        else:
            print("코코팜 수량이 부족합니다.")
    elif select==2:
        if coca_cola.quantity>0:
            order(coca_cola, money)
        else:
            print("코카콜라 수량이 부족합니다.")
    elif select==3:
        if tomato_juice.quantity>0:
            order(tomato_juice, money)
        else:
            print("토마토주스 수량이 부족합니다.")
    else:
        print("음료를 잘못 선택하셨습니다. ")      
        
def order(drink, money):
    if money>= drink.price:
        money = money-drink.price
        print("%s을 선택하셨습니다. 거스름돈은 %d"% (drink.name, money))
        drink.sub_quantity()
    else:
        print("금액이 부족합니다")
        
def service_manager(select):
    action = int(input("<1>수량 늘리기 <2>수량 줄이기"))
    if select==1:
        if action==1:
            cocofarm.add_quantity()
        elif action==2:
            cocofarm.sub_quantity()
    elif select==2:
        if action==1:
            coca_cola.add_quantity()
        elif action==2:
            coca_cola.sub_quantity()
    elif select==3:
        if action==1:
            tomato_juice.add_quantity()
        elif action==2:
            tomato_juice.sub_quantity()
    else:
        print("잘못 입력했습니다.")
        
        
if __name__ == "__main__":
    while True:
        type = int(input("당신은 누구입니까? <1> 관리자 <2> 고객 "))
        select =  int(input("음료를 골라주세요\n 1.코코팜 700원 2.코카콜라 1000원 3. 토마토주스 300원"))
        if type == 1:
            service_manager(select)
        elif type == 2:
            service_customer(select)
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요")