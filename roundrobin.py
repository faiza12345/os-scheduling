
a=[]
waitingtime=[]
remainingburst=[]
turnaround=[]


qtm=int (raw_input('Enter time quantum: '))
n=int(raw_input('Total number of processes: '))



for i in xrange(n):
	a.append([])
	a[i].append(raw_input('enter process name: '))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))

# for calculating waiting time
a.sort(key=lambda a:a[1])
for i in xrange(n):
	remainingburst[i]=a[i][2]
	currenttime=0
for i in xrange(n):
	if remainingburst[i]>qtm
		currenttime+=qtm
		remainingburst[i]-=qtm;
	else:
		currenttime=currenttime+remainingburst[i]
		waitingtime[i]=currenttime-a[i][2]
#for calculating turn around time

for i in xrange(n):
	turnaround[i]=a[i][2]+waitingtime[i]


print 'Process \t Arrival time \t Burst time \t waiting time \t turnaround time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',a[i][4]-a[i][1]-a[i][2],'\t\t', turnaround[i]