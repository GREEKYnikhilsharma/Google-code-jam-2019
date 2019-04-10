val = input()
op_list = []
for i in range(1,val):
 input1 = input()
 str_input = str(input1)
 buf = 0
 for ii in range(len(str_input)):
   if str_input[ii] == "4":
     buf += 2 * pow(10, len(str_input) - 1 - ii)
 op1 = input1 - buf
 op_list.append("Case #"+ str(i) + ":" + str(op1) + " " + str(buf))

for i in op_list:
 print(i)
