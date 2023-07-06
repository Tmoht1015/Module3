# Dependencies
import csv 
#csv read
with open ('budget_data.csv') as csvfile: 

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Variables and Conditions
    months=[] 
    prolosses=[] 

   
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    #Read
    for row in csvreader:
        month=row[0] 
        proloss=row[1] 
        months.append(month) 
        prolosses.append(proloss) 
    
    m_count = len(months) 


#analysis

#loop1
for loop1 in range (m_count):
    total=total+int(prolosses[loop1]) 

#loop2 (calculation)
for loop2 in range (m_count-1): #Restrict loop to avoid overflow (last line +1)
    a_change=a_change+(float(prolosses[loop2+1])-float(prolosses[loop2])) 

    m_change=(float(prolosses[loop2+1])-float(prolosses[loop2])) 
    if m_change>delta1: 
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

    if m_change<delta2: 
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2

#output

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

print(analysis) 

#txt file

file1=open("pybank.txt","w") 
file1.writelines(analysis) 
file1.close() 