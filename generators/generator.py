# def square_numbers(*nums):
#     for i in nums:
#         yield (i*i)


# my_nums = square_numbers(*[1, 2, 3, 4, 5])


# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

##

# my_nums = square_numbers(*[1, 2, 3, 4, 5])
# for num in my_nums:
#     print(num)

## Generator expressions


my_nums = list(x*x for x in [1,2,3,4,5])
my_sum = sum([x*x for x in range(1,10)])

# print (my_nums)
# print (my_sum)

# jobtext = '/administrator/ HTTP/1.1'
# all_lines = (line for line in open('..\\scripts\\access.log', 'r') )
# job = ( line for line in all_lines if line.find(jobtext) != -1)
# print(next(job))
# print(next(job))
# print(next(job))