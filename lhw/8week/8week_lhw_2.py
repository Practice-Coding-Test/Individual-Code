import os
customer_data = {'A':10000, 'B':5000, 'C':200000, 'D':10000, 'E':500, 'F':300000, 'G':50000, 'H':7000, 'J':9000}

if not os.path.isdir("customer"):
    os.mkdir('customer')

with open("customer/vip_list.txt", 'w', encoding='utf-8') as f:
    for key, value in customer_data.items():
        if value >= 10000:
            f.write(key + " " +str(value) +  '\n')
