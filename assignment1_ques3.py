# numbers = (1,2,3,4,5,6,7,8,9)
# print("even and odd tup item =",numbers)

# even_count = odd_count = 0

# for i in range(len(numbers)):
#     if (numbers[i] % 2 == 0):
#         even_count = even_count+ 1
#     else:
#         odd_count =odd_count+ 1

# print("even count:",even_count)
# print("odd count:",odd_count)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print('list of numbers :',numbers)
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print('even count :',even_count)
print('odd_count :',odd_count)

    
    
     
