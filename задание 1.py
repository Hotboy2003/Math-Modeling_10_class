def vis_func(a):
    """ m;lm;lm """
    
    if a%4==0 and a%100==0 and a%400==0:
        print('Год високосный')
    else:
        print('Год не високосный')
    return a

vis_func(2001)
