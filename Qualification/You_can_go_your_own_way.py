val = input()
op_list = []
for i in range(1,val + 1):
 input1 = input()
 input2 = raw_input()
 buf = ""
 for ii in input2:
   if ii == "S":
     buf = buf + "E"
   elif ii == "E":
     buf = buf + "S"
 op_list.append("Case #"+ str(i) + ":" + " " + str(buf))

for i in op_list:
 print(i)
