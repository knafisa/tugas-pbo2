total = 0 #ini variabel global
def sum(arg1, arg2):
    total = arg1 + arg2
    print('Inside the function: {}'.format(total))
    return total
sum(10,20)
print('Outside the function: {}'.format(total))

total = 0 #ini variabel global
def sum(arg1, arg2):
    global total
    total = arg1 + arg2
    print('Inside the function local total: ', total)
    return total
sum(10, 20)
print('Outside the function (global) total: ', total)