

pq = int(input("Enter PQ : "))
key = int(input("Enter Key : "))
m = int(input("Enter m : "))

exp = m ** key
encrypted_message = exp % pq
print('Your de/encrypted message is: ' + str(encrypted_message))


input()