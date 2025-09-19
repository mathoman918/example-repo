# input the minutes taken in the triathlon events swimming, cycling, and running
swimming = int(input("How many minutes taken for swimming?"))
cycling = int(input("How many minutes taken for cycling?"))
running = int(input("How many minutes taken for running?"))
#calculate and output the total time to complete the triathlon
triathlon_award= swimming + cycling + running
#award for finishing Within the qualifying time.
# Provincial colours
if triathlon_award <= 100:
 print ("Provincial colours")
#award for finishing Five minutes off from the qualifying time.
elif triathlon_award <= 105:
 print ("Provincial half colours")
#award for finishing 10 minutes off from the qualifying time.
elif triathlon_award <= 110:
 print ("Provincial scroll")
#award for finishing More than 10 minutes off from the qualifying time.
else:
 print ("no award")