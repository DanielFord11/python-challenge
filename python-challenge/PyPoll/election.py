import csv
import os

votes=[]


f = open("election_data.csv", "r")

reader = csv.reader(f)
next (reader, None)

for row in reader:
    votes.append(row[2])


TotalVotes = len(votes)

KhanCount = votes.count("Khan")
KhanMargin = "{0:.0%}".format(round(KhanCount/len(votes),4))

CorreyCount = votes.count("Correy")
CorreyMargin = "{0:.0%}".format(round(CorreyCount/len(votes),4))

LiCount = votes.count("Li")
LiMargin = "{0:.0%}".format(round(LiCount/len(votes),4))

OTooleyCount = votes.count("O'Tooley")
OTooleyMargin = "{0:.0%}".format(round(OTooleyCount/len(votes),4))


#prints results to terminal

print (f''''

Election Results
-------------------------
Total Votes: {TotalVotes}
-------------------------
Khan: {KhanMargin} ({KhanCount})
Correy: {CorreyMargin} ({CorreyCount})
Li: {LiMargin} ({LiCount})
O'Tooley: {OTooleyMargin} ({OTooleyCount})
-------------------------
Winner: Khan
-------------------------
''')


output_file = os.path.join("ElectionResult.txt")

output_file = open("ElectionResult.txt", "w")

output_file.write(f'''

Election Results
-------------------------
Total Votes: {TotalVotes}
-------------------------
Khan: {KhanMargin} ({KhanCount})
Correy: {CorreyMargin} ({CorreyCount})
Li: {LiMargin} ({LiCount})
O'Tooley: {OTooleyMargin} ({OTooleyCount})
-------------------------
Winner: Khan
-------------------------
''')

output_file.close()







