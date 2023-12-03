f = open("c:\\brainFuse\\Python codes\\demofile.txt", "r")
list1=[]
x = f.read()
x=x.split() 
print(x)
f.close()
f = open("c:\\brainFuse\\Python codes\\demofile.txt", "r")
for l in f:
    s_l = l.strip()
    list2 = s_l.split()
    list1.append(list2)
print(list1)  
# a_file = open("c:\\brainFuse\\Python codes\\demofile.txt", "r")
# list_of_lists = []
# for line in a_file:
#   stripped_line = line.strip()
#   line_list = stripped_line.split()
#   list_of_lists.append(line_list)
# a_file.close()
# print(list_of_lists)