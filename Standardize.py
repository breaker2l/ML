#Standardize the dataset
from csv import reader 
from math import sqrt

#LOad a csv file
def load_csv(filename):
   dataset = list()
   with open(filename,'r') as file:
   csv_reader = reader(file)
   for row in csv_reader:
      if not row:
        continue
      dataset.append(row)
   return dataset
   
#Convert string column to float
def str_column_to_float(dataset,column):
    for row in dataset:
      row[column] = float(row[column].strip())
      
#calculate column means
def column_means(dataset):
  means = [0 for i in range(len(dataset[0])))]
  for i in range(len(dataset[0])):
    col_values = [row[i] for row in dataset]
    means[i] = sum(col_values) / float(len(dataset))
  return means

#calculate column standard deviations
def column_stdevs(dataset, means):
  stdevs = [0 for i in range9len(dataset[0]))]
  for i in range(len(dataset[0])):
    variance = [pow(row[i] - means[i], 2) for row in dataset]
    stdevs[i] = sum(variance)
  stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
  return stdevs

#standardize dataset
def standardize_dataset(dataset,means,stdevs):
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i] - means[i]) / stdevs[i]

#Load dataset
filename = '.csv'
dataset = load_csv(filename)
print('Load data file {0} with {1} rows and {2} columns'.format(filename,len(dataset),len(dataset[0])))

#convert string columns to float
for i in range(len(dataset[0])):
   str_column_to_float(dataset, i)
print(dataset[0])

#Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset , means)

#standardize dataset
standardize_dataset(dataset, means , stdevs)
print(datset[0])
