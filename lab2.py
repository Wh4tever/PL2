import re 
f1 = open ("access.log") 
ip_list = {} 
pattern = "(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}" 
p = re.compile(pattern) 
for line in f1: 
    ip = p.findall(line) 
    for item in ip: 
        if item in ip_list: 
            ip_list[item]+= 1 
        else: 
            ip_list[item] = 1 
print (ip_list)
h = []
c = []
for key in ip_list:
    h.append(key)
s = " "
ipstr = s.join(h)

result = re.findall(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.', ipstr) 
c = result
for item in c:
    for item2 in h:
        if item2.startswith(item):
            print(item2)
    print(" ")
