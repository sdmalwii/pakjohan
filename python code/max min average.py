#numbers = [3, 5, 1, 9, 2]
#max_number = max(numbers)
#print(max_number) # Output: 9 
#numbers = [3, 5, 1, 9, 2]
#min_number = min(numbers)
#print(min_number) # Output: 1
#average = sum(numbers) / len(numbers)
#print(average) # Output: 4.0
numbers = [5, 10, 3, 8, 6, 1]
n = 3 # mencari 3 nilai tertinggi
top_n = sorted(numbers, reverse=True)[:n]
print(top_n) # Output: [10, 8, 6]