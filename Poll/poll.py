# Dependencies
import csv 
#csv read
with open ('election_data.csv') as csvfile: 

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Variable/List Creation 
    voterids=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 

    #loop start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Read 
    for row in csvreader:
        voterid=row[0] 
        county=row[1] 
        candidate=row[2] 
        voterids.append(voterid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    line_count= len(voterids) 
    


#Analysis
candidatenames.append(candidates[0]) #Pre-loadfirst candidate name for comparison
#loop1
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)
#loop2
for loop2 in range (n): 
    totaleachcan.append(candidates.count(candidatenames[loop2])) 

#loop3

loservotes=line_count 

for loop3 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
    if totaleachcan[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    if totaleachcan[loop3]<loservotes: 
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]

#loop4
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') #Format list resultprintcan

resultlines='\n'.join(resultprintcan) 

#Output
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} \n\
Last: {loser} \n\
----------------------------\n'

print(analysis) 

#txt file

file1=open("pypoll.txt","w") 
file1.writelines(analysis) 
file1.close() 