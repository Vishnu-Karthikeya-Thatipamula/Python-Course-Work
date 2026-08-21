'''
print("=======MENU========")
data = {
         'Facewash':80,
         'cookingoil':180,
         'Rice':500,
         'egg':36,
         'Milk':32,
         'coconutoil':50,
         'snacks':50,
         'sugar': 100
         
}
for i in data:
    print(i.ljust(20), data[i])

prods = input("Enter the products:").split()
prods_lst = list(prods)
total = 0
for i in prods_lst:
    print(i.ljust(20),data[i])
    total += data[i]
print("Your bill is ", total)


'''

s = input("Enter the string")
res = ''
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i+1]: 
        count += 1
    else:
        res += s[i] + str(count)
        count = 1
print(res + s[-1] + str(count))



#assert
email = ''
password = ''


    
