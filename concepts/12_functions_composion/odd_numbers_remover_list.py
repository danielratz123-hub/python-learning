def is_even(number):
    return number %2 ==0

def count_evens_in_list(numbers):
    count = 0
    for n in numbers:
        if is_even(n):
            count+=1
    return count

numbers =[5,2,7,14,27,98]
result = count_evens_in_list(numbers)
print(F"the even numbers amount is{result}")