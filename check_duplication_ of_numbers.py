with open("shelly job.txt", 'r')as f:
    content = f.read()

content_list = content.split('\n')  #converts string into list by newline(\n) separator

def checkDupli(list):
    duplicate_numbers = set()
    for i in list:
        if list.count(i) > 1:
            duplicate_numbers.add(i)
    return duplicate_numbers

result = checkDupli(content_list)

print(result)
