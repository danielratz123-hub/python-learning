def calculated_stats(numbers):
    end_amount = sum(numbers)
    average = round(sum(numbers) / len(numbers),2)
    highest= max(numbers)
    return end_amount , average , highest

numbers = [5,7,6,98,13,65]
end_amount , average , highest = calculated_stats(numbers)

print(f"The sum of the list is:{end_amount}")
print(f"The average of the list is: {average}")
print(f"The max number of te list is:{highest}")