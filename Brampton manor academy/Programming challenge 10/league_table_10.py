import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary={}
    
    for row in rows:
        home,away,homegoals,awaygoals,winner=row[1],row[2],row[3],row[4],row[5]
        if home not in dictionary:
            dictionary[home]=[0,0,0,0,0] ## win,draw,lost,goal diff, points
        if away not in dictionary:
            dictionary[away]=[0,0,0,0,0] ## win,draw,lost,goal diff, points
        if winner=="D":
            dictionary[home][4]+=1
            dictionary[away][4]+=1
            dictionary[home][1]+=1
            dictionary[away][1]+=1
        if winner=="H":
            dictionary[home][4]+=3
            dictionary[home][0]+=1
            dictionary[away][2]+=1
        if winner=="A":
            dictionary[away][4]+=3
            dictionary[away][0]+=1
            dictionary[home][2]+=1
        dictionary[home][3]=dictionary[home][3]+(int(homegoals)-int(awaygoals))
        dictionary[away][3]=dictionary[away][3]+(int(homegoals)-int(awaygoals))
        
    return dictionary

def statistics(rows):
  statistics={}
  for row in rows:
    homeshots,awayshots,homeshotsontarget,awayshotsontarget,homefouls,awayfouls=row[7],row[8],row[9],row[10],row[11],row[12]
    home,away=row[1],row[2]
    
    if home not in statistics:
      statistics[home]=[0,0,0,0,0]
      
    if away not in statistics:
      statistics[away]=[0,0,0,0,0]
  
    statistics[home][0]+=int(homeshots)
    statistics[away][0]+=int(awayshots)
    statistics[home][1]+=int(homeshotsontarget)
    statistics[away][1]+=int(awayshotsontarget)
    statistics[home][2]+=int(homefouls)
    statistics[away][2]+=int(awayfouls)
    statistics[home][3]=statistics[home][1]/statistics[home][0]
    statistics[away][3]=statistics[away][1]/statistics[away][0]
    statistics[home][4]=statistics[home][2]/38
    statistics[away][4]=statistics[away][2]/38
  return statistics

def referee(rows):
  referee={}
  for row in rows:
      ref,homeyellow,awayyellow,homered,awayred=row[6],row[15],row[16],row[17],row[18]
      if ref not in referee:
       referee[ref]=[0,0,0]
      card=int(row[15])+int(row[16])+(3*int(row[17]))+(3*int(row[18]))
      referee[ref][0]+=card
      referee[ref][1]+=1
  return referee

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    myDict=(process_results(file_contents))
    statistic=statistics(file_contents)
    refer=referee(file_contents)
    print(f"{'Team':<20} {'Wins':<10} {'draws':<10} {'losses':<10}{'GD':<10}{'Points':<10}")
    for key,value in sorted(myDict.items(), key=lambda e: e[1][4],reverse=True):
        print(f"{key:<20} {value[0]:<10} {value[1]:<10} {value[2]:<10} {value[3]:<10}{value[4]:<10}")
    sortaccuracy= sorted(statistic.items(), key=lambda e: e[1][3])
    print(f'the most accurate team is {sortaccuracy[19][0]}')
    print(f'the least accurate team is {sortaccuracy[0][0]}')
      
    sortreferee=sorted(refer.items(), key=lambda e: e[1][0])
    print(f'the referee with the highest card avearge per game is {sortreferee[19][0]}')
    print(f'the referee with the lowest card avearge per game is {sortreferee[0][0]}')
    sortedfouls=sorted(statistic.items(), key=lambda e: e[1][4])
    print(f'the team with the most fouls per game is {sortedfouls[19][0]}')
    print(f'the team with the least avearge per game is {sortedfouls[0][0]}')
  
    

 


    
   
