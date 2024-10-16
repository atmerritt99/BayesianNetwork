import BayesianNetwork

model = BayesianNetwork.BayesianNetwork()
training_data = []
                    
with open("data\BurglaryAlarmExampleData.csv", "r") as data_file:
    data_lines = data_file.readlines()

    for line in data_lines[1:]: #Ignore header
        x = line.strip() #Remove Newline
        data = tuple(map(int, x.split(','))) #Convert to numerical data
        training_data.append(data)

model.train(training_data)

query = (None, None, None, 1, 1)
givens = (1, None, None, None, None)

#What is the probability that John and Mary call given a burglary
print(model.get_probability(query, givens))