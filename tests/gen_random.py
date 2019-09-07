import random

for i in range(400):
    ran_num = random.randint(0, 18446744073709552000)
    print('{0:0{1}X}'.format(ran_num, 16))
