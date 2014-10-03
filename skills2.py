"""Functions refactored to work with map, reduce, filter"""
# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]
#number_list2 = [-4, 2, 16, 8, 22, 5, 101, 2, 22, 7, 50]
#word_list2 =[ "Hey", "there", "what", "are", "hey", "doing", "whatever", "interesting", "kangaroo", "no"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.

def all_odd(number_list): 

    def odd(num):
        if num % 2 != 0:
            return num

    numbers = filter(odd, number_list)

    return numbers


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    
    def even(num):
        if num % 2 == 0:
            return num

    numbers = filter(even, number_list)

    return numbers

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):

    def long(word):
        if len(word) >= 4:
            return word

    words = filter (long, word_list)

    return words


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):

    x = reduce(min, number_list)
    return x


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):

    x = reduce(max, number_list)
    return x



# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    
    def halve(number):
        return number/2.0

    numbers = map(halve, number_list)

    return numbers


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):

    def lengths(word):
        return len(word)
    
    words = map(lengths, word_list)

    return words




# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    count = 0
    for number in number_list:
        count += number

    return count



# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    
    count = 1

    for number in number_list:
        count*=number

    return count



# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    
    joined = ''

    for word in word_list:
        joined += word + ' '

    return joined



# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    count = 0

    for number in number_list:
        count += number

    mean = float(count)/len(number_list)

    return mean



