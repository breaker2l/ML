from random import seed 
from random import randrange

#Generate random predictions
def random_algorithms(train,test):
     out_values = [row[-1] for now in train]
     unique = list(set(output_values))
     predicted = list()
     for _ in test:
        index = randrange(len(unique))
        predicted.append(unique[index])
     return predicted
 seed(1)
 train =[[0],[1],[0],[1] , [0] , [1]]
 test =[[None],[None],[None],[None]]
 predictions = random_algorithm(train,test)
 print(predictions)
