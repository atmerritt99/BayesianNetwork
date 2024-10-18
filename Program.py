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

query = (1, 1, None, None, None)
givens = (None, None, 0, 1, 1)

#What is the probability of a burglary and earthquake given John and Mary call but theres no alarm
print(model.bayes_eval(query, givens))
print(model.bayes_eval(query, givens, .5))

#Remove this node, so later I can simulate a use case for the clarity variable
del model.bayesian_nodes[(1,1,0,1,1)]

print(model.bayes_eval(query, givens))
print(model.bayes_eval(query, givens, .5))