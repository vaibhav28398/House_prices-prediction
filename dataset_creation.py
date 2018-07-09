def dataset(builder):
    import csv
    f=open('%s.txt' %builder,"r");
    target={"id1":"NaN","datebuilt":"NaN","datepriced":"NaN","garden":"NaN","dock":"NaN","capital":"NaN","royalmarket":"NaN","guardingtower":"NaN","river":"NaN","renovation":"NaN","dining":"NaN","bedroom":"NaN","bathroom":"NaN","kingvisit":"NaN","curse":"NaN","blessing":"NaN","farmland":"NaN","location":"NaN","holytree":"NaN","knighthouse":"NaN","builder":"NaN","price":"NaN"}
    location={"King's Landing":"0","The Mountains":"1","Servant's Premises":"2","Cursed Land":"3"}
    builders={"Bob":"0","Bright_Brothers":"1","The_Greens":"2","The_Lannisters":"3","The_Kings":"4","The_Ollivers":"5","The_Overlords":"6","The_Starks":"7","Wood_Priests":"8","Masters_of_Stones":"9","Not_Known":"NaN"}

        
    l=1
    for line in f:
        if line=="\n":
            if l==1:
                c=[]
                target["builder"]=builders[builder]
                with open("house_prices.csv","r") as f:
                    reader=csv.reader(f);
                    for row in reader:
                        if row[0]==target["id1"]:
                            target["price"]=row[1]
                            break
                for x in target:
                    c.append(target[x])
                    target[x]="NaN"
                with open("final_dataset.csv","a") as csvfile:
                        data_csv=csv.writer(csvfile)
                        data_csv.writerow(c)
                l=2
        else:
            l=1
            if "ID" in line:
                target["id1"]=line[12:20]
            elif "Date" in line:
                target["datebuilt"]=line.split(" ")[3].split("/")[2]
                target["datepriced"]=line.split(" ")[11].split("/")[2]
            elif "garden" in line:
                if "no" in line:
                    target["garden"]="0"
                else:
                    target["garden"]="1"
            elif "Dock" in line:
                target["dock"]=line.split(" ")[5]
            elif "Capital" in line:
                target["capital"]=line.split(" ")[4]
            elif "Royal" in line:
                target["royalmarket"]=line.split(" ")[5]
            elif "Guarding" in line:
                target["guardingtower"]=line.split(" ")[5]
            elif "River" in line:
                target["river"]=line.split(" ")[5]
            elif "renovation" in line:
                if "not" in line:
                    target["renovation"]="0"
                else:
                    target["renovation"]="1"
            elif "dining" in line:
                target["dining"]=line.split(" ")[2]
            elif "bedrooms" in line:
                target["bedroom"]=line.split(" ")[2]
            elif "bathrooms" in line:
                target["bathroom"]=line.split(" ")[2]
            elif "visit" in line:
                target["kingvisit"]="0"
            elif "Visited" in line:
                target["kingvisit"]="1"
            elif "cursed" in line:
                target["curse"]="1"
            elif "curse" in line:
                target["curse"]="0"
            elif "blessed" in line:
                target["blessing"]=line.split(" ")[5]
            elif "farm" in line:
                if "no" in line:
                    target["farmland"]="0"
                elif "huge" in line:
                    target["farmland"]="2"
                else:
                    target["farmland"]="1"
            elif "Location" in line:
                target["location"]=location[line[27:len(line)-1]]
            elif "Holy" in line:
                if "cut" in line:
                    target["holytree"]="0"
                else:
                    target["holytree"]="1"
            elif "Knight\'s" in line:
                target["knighthouse"]=line.split(" ")[5]
import csv
c=[]
target={"id1":"-1","datebuilt":"-1","datepriced":"-1","garden":"-1","dock":"-1","capital":"-1","royalmarket":"-1","guardingtower":"-1","river":"-1","renovation":"-1","dining":"-1","bedroom":"-1","bathroom":"-1","kingvisit":"-1","curse":"-1","blessing":"-1","farmland":"-1","location":"-1","holytree":"-1","knighthouse":"-1","builder":"-1","price":"-1"}
for x in target:
    c.append(x)
with open("final_dataset.csv","a") as csvfile:
    data_csv=csv.writer(csvfile,delimiter=',')
    data_csv.writerow(c);                
files={"Bob","Bright_Brothers","The_Greens","The_Lannisters","The_Kings","The_Ollivers","The_Overlords","The_Starks","Wood_Priests","Masters_of_Stones","Not_Known"}
print "Your file is being created";
for builder in files:
    dataset(builder)

#Sorting the created datatset according to the House id by converting it in integer(it is hexadecimal)


import pandas as pd
dataset=pd.read_csv('final_dataset.csv',converters={'id1':lambda x: int(x,16)});
dataset.sort_values(by=['id1'],inplace=True)
dataset.to_csv('final_dataset.csv',index=False);

print "A file name final_dataset.csv will be created which the dataset of this code";