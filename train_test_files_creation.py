import csv
i=-1
target={"id1":"-1","datebuilt":"-1","datepriced":"-1","garden":"-1","dock":"-1","capital":"-1","royalmarket":"-1","guardingtower":"-1","river":"-1","renovation":"-1","dining":"-1","bedroom":"-1","bathroom":"-1","kingvisit":"-1","curse":"-1","blessing":"-1","farmland":"-1","location":"-1","holytree":"-1","knighthouse":"-1","builder":"-1","price":"-1"}
with open("test.csv","a") as test:
    writer=csv.writer(test)
    writer.writerow(target.keys())
with open("train.csv","a") as train:
    writer=csv.writer(train)
    writer.writerow(target.keys())
with open("final_dataset.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        i=i+1
        if row["price"]=="":
            with open("test.csv","a") as test:
                writer=csv.writer(test)
                writer.writerow(row.values())
        else:
            with open("train.csv","a") as train:
                writer=csv.writer(train)
                writer.writerow(row.values())
        
print "Two files one named train.csv which has the training data and other named test.csv which has the testing data will be created";