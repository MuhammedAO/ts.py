# an exponent functional is gonna allow us to take a number and raise it to a specific power

# print(4**4)


# we don't know right off the bat what the pow_num is going to be. the user will decide that
# multiply the base_num by itself as many times as the pow_num specifies
# result store the actual result of the math
# loop through the for-loop as many times as pow_num
# first time through the loop, result is 1. second time, result * basenum which is essentially basenum * basenum

def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result


print(raise_to_power(5,5))  
  
  