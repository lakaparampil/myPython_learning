print(" ")
print("Table of Contents:")
print("------------------------------------------------------------ ")
print("1. Return the first duplicate in a list")
print("2. Check wheter a number is a palindrome or not")
print("3. Sort a dictionary by values")
print("4. Return all prime numbers in a given range")
print("5. Convert a list of numbers to a string")
print("------------------------------------------------------------ ")
my_input = input("Enter one choice number:(1/2/3/.....):  ")
print("------------------------------------------------------------ ")
match my_input:
    case "1":
        def first_duplicate(lst):
            seen = set()
            for num in lst:
                if num in seen:
                    return num
                seen.add(num)
            return None
        print(first_duplicate([2, 3, 3, 1, 5, 2]))
    case "2":
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        print(is_palindrome(121))
        print(is_palindrome(123))
    case "3":
        def sort_dict_by_values(d):
            return dict(sorted(d.items(), key=lambda item: item[1]))
        print(sort_dict_by_values({'apple': 3, 'banana': 1, 'cherry': 2}))
    case "4":
        def primes_in_range(start, end):
            primes = []
            for num in range(start, end + 1):
                if num > 1:
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            break
                    else:
                        primes.append(num)
            return primes
        print(primes_in_range(10, 50))
    case "5":
        def list_to_string(lst):
            return ''.join(map(str, lst))
        print(list_to_string([1, 2, 3, 4, 5]))
print("Like to continue(y/n)?")
if input().lower() == 'y':
    exit()
exit()
