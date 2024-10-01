nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i_sqa = [num*num for num in nums]
print(i_sqa)

'''
if num of elements in input n num of elements in output are not equal
then some filtering is happening and hence we shd apply some condition in comprehension
if its equal, no need of condition
'''

tech_stack = ('Java', 'C++', 'Python', 'Scala',  '.Net', 'Hadoop', 'PySpark', 'C', 'Cassandra', 'Kafka', 'Go')

res = [word.upper() for word in tech_stack if len(word) > 4]
print(res)

res1 = r = [len(word) for word in tech_stack if len(word) >= 4]
print(res1)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # [4, 16, 64, 100]

res3 = [x*x for x in nums if x % 2 == 0]
print(res3)

#accessing the elements of list
tech_stack = ['Spark', 'Measos', 'Akka', 'Cassandra', 'Kafka', 'Hadoop']

print('tech_stack[0] = ', tech_stack[0])
print('tech_stack[-6] = ', tech_stack[-6])

print('tech_stack[4] = ', tech_stack[4])
print('tech_stack[-2] = ', tech_stack[-2])

#print('tech_stack[-20] = ', tech_stack[-20])  #IndexError
print('tech_stack[5] = ', tech_stack[5])
print('tech_stack[-1] = ', tech_stack[-1])