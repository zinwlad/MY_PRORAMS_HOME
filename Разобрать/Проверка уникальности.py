def unique(l):
    if len(l) == len(set(l)):
        print('Все элементы уникальны')
    else:
        print("Не уникальны")
unique([1,2,3,4])
unique([1,1,3,4])