import csv
import math

class KNN:
  def __init__(self):
    self.k = 0
  
  def eud(self,x,y):
    d = 0
    for i in range(0,len(y)):
      d += (float(x[i])-float(y[i]))**2
    return math.sqrt(d)

  def knn(self,trainData,testData,k):
    self.k = k
    for test in testData:
      distances = []
      for train in trainData:
        d = self.eud(train,test)
        distances.append([d,train])
      distances.sort(key = lambda x:x[0])
      print(distances)
      neighbors = []
      for i in distances[:self.k]:
        neighbors.append(i[1])
       
      print(neighbors)
      classes = {}
      for neigh in neighbors:
        label = neigh[-1]
        if(label not in classes.keys()):
          classes[label]=0
        classes[label]+=1
      predictedClass = max(classes,key=lambda x:classes[x])
      print(predictedClass)

file = open("/content/data.csv",'r')

csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

train = []
for i in csvreader:
  r1 = float(i[0])
  r2 = int(i[1])
  r3 = int(i[2])
  train.append([r1,r2,r3,i[3]])
print(train[:5])

test = [[9,8,0]]

knn = KNN()

knn.knn(train,test,3)