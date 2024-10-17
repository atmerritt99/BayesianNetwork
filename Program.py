import BayesianNetwork

model = BayesianNetwork.BayesianNetwork()
'''
training_data = []
                    
with open("data\BurglaryAlarmExampleData.csv", "r") as data_file:
    data_lines = data_file.readlines()

    for line in data_lines[1:]: #Ignore header
        x = line.strip() #Remove Newline
        data = tuple(map(int, x.split(','))) #Convert to numerical data
        training_data.append(data)

model.train(training_data)

model.save('burglary_alarm_bayesian_model.txt')
'''

model.load('burglary_alarm_bayesian_model.txt')

query = (1, None, None, None, None)
givens = (None, None, None, 1, 1)

#What is the probability of a burglary given John and Mary call
print(model.get_probability(query, givens))