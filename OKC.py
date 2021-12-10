
import csv

def dist(x, y):
    return (x**2 + y**2)**0.5

class Team:
    def __init__(self, name):
        self.name = name
        self.pt2Made = 0
        self.pt2Atmpt = 0
        self.nc3Made = 0
        self.nc3Atmpt = 0
        self.c3Made = 0
        self.c3Atmpt = 0

    #check div by 0 error

    
    # Method to calculate what zones points are shot in
    def shot(self, x, y, made):
        # c3 is the corner
        if((x > 22.0 or x < -22.0) and y < 7.8):
            self.c3Made += made;
            self.c3Atmpt += 1;

        # non-corner 3 point shot outside of the 3 line
        elif(dist(x, y) > 23.75 and x > 0 and y > 0):
            self.nc3Made += made
            self.nc3Atmpt += 1

        # 2pt
        else:
            self.pt2Made += made
            self.pt2Atmpt += 1



file = open("C:\\Users\\jhtra\\Downloads\\shots_data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

# dictionary for team names to map to stat sheet
teams = {}

for row in rows:
    team_name = row[0]
    x = float(row[1])
    y = float(row[2])
    made = int(row[3])

    if team_name in teams:
        team = teams[team_name]
        team.shot(x, y, made)
        
    else:
        teams[team_name] = Team(team_name)
        team = teams[team_name]
        team.shot(x, y, made)

for team in teams:
    print(team + ":")
    print("2PT zone shots: " + str(teams[team].pt2Atmpt / (teams[team].pt2Atmpt+teams[team].nc3Atmpt+teams[team].c3Atmpt)))
    print("NC3 zone shots: " + str(teams[team].nc3Atmpt / (teams[team].pt2Atmpt+teams[team].nc3Atmpt+teams[team].c3Atmpt)))
    print("C3 zone shots: " + str(teams[team].c3Atmpt / (teams[team].pt2Atmpt+teams[team].nc3Atmpt+teams[team].c3Atmpt)))
    print("eFT in 2PT: " + str(teams[team].pt2Made / teams[team].pt2Atmpt))
    print("eFT in NC3: " + str(1.5 * teams[team].nc3Made / teams[team].nc3Atmpt))
    print("eFT in C3: " + str(1.5 * teams[team].c3Made / teams[team].c3Atmpt))
