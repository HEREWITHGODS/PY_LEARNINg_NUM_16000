def even_only(numbers):
    even_numbers = [num for num in numbers if num%2==0]
    return even_numbers

print(even_only([1,2,3,4,5,6,7,8,9]))