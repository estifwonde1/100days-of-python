def add(*args):
    m =0
    for n in args:
        m += n

    return(m)
print(add(1,2,3,4,5,6,7,8,))

def calculate(**kwargs):
    print(kwargs)

calculate(add = 5 , multiply = 10)