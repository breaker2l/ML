#Sonar Dataset
Download : https://goo.gl/FXFWwF
Top Results: https://goo.gl/3wNAjv

#Random Forest Algorithm on sonar dataset
from random import seed 
from random import randrange
from csv import reader
from math import sqrt

#Load a csv file
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

#Convert string column to integer
def str_column_to_int(dataset,column):
    class_values = [row[column] for row in dataset]
    unique = set(class_vlaues)
    lookup = dict()
    for i,value in enumerate(unique):
       lookup = dict()
    for row in dataset:
       row[column] = lookup[row[column]]
    return lookup

#split a dataset into k folds
def cross_validation_split(dataset, n_folds):
  dataset_split = list()
  dataset_copy = list(dataset)
  fold_size = int(len(dataset)) / n_folds)
  for _ in range(n_folds):
    fold = list()
    while len(fold) < fold_size:
      index = randrange(len(dataset_copy))
      fold.append(dataset_copy.pop(index))
    dataset_split.append(fold)
  return dataset_split

#claculate accuracy percentage
def accuracy_metric(actual,predicted):
  coorect = 0 
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct += 1
  return correct / float(len(actual)) * 100.0

