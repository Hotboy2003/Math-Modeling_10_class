from my_module import cv
m=1.4*10**21 

def armageddon_func(ma, V):
    T=(ma*V**2)/(2*cv*m)
    if T>=50:
        print('YOU DIED')
    elif T>=30 and T<50:    
        print('90% BIOMASSY DIED')
        a=((cv*m*100*2)/ma)**0.5
        print(a)
    else:
        a=((cv*m*100*2)/ma)**0.5
        print(a)
        print('ВЫ ПОЛУЧИЛИ УРОН, ЧТОБЫ ВОССТАНОВИТЬ ЗДОРОВЬЕ, ВАМ НУЖНО ПОСПАТЬ ИЛИ ПОЕСТЬ')
        
armageddon_func(50000000000, 45454645)