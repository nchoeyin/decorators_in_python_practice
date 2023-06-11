def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result
new_num = plus_one(4)
print(new_num)

"""
Output :
5
"""
