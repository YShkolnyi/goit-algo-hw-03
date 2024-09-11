from datetime import datetime
import random
import re

def get_days_from_today(date):
    try:
        date_conv  = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        delta =  current_date - date_conv
        delta = int(delta.days)
        return delta
    except ValueError: 
        print("Correct form is: 'yyyy-mm-dd'. Try again ;)")
    except TypeError:
        print("Correct form is: 'yyyy-mm-dd'. Try again ;)")

def get_numbers_ticket(min=1, max=1000, quantity=1):
    list=[]
    rules='\tWe have three rules:\n\t\t1. 1<= min < max <=1000\n\t\t2. quantity <= (max-min)\n\t\t3. Only INT arguments'
    try:
         if min>=1 and max<=1000 and min<max and quantity<=(max-min):
            for i in range(max-min+1):
                list.append(min)
                min +=1
            lotery = random.sample(list, k=quantity)
            lotery.sort()
            return lotery
         else:
            print(rules)
            return list
    except TypeError:
         print(rules)
         return list

def normalize_phone(phone_number):
     pattern = r'\D'
     formated_numbers = []
     short_numbers = []
     sanitized_numbers = []
     count = 0

     while count < len(phone_number):
         formated_numbers.append(re.sub(pattern, '', phone_number[count]))
         short_numbers.append(formated_numbers[count].removeprefix('38'))
         number=['+38',short_numbers[count]]
         sanitized_numbers.append(''.join(number))
         count += 1
     return sanitized_numbers

# qwerty