import random
def get_numbers_ticket(min,max,quantity):
    row=[]
    if min<1 or max>1000:
        return row
    
    for num in range(min,max):
        row.append(num)
    
    rand_row=random.sample(row,quantity)
    rand_row.sort()

    return rand_row
    
     
lottery_numbers = get_numbers_ticket(1, 46, 6)
print("Ваші лотерейні числа:", lottery_numbers)

