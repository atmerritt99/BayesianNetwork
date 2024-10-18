class BayesianNetwork:

    def __init__(self):
        self.bayesian_nodes = {}

    def load(self, file_name):
        self.bayesian_nodes = {}

        with open(file_name, 'r') as network_file:
            lines = network_file.readlines()
            
            for line in lines:
                stripped_line = line.strip() #Remove Newline

                tokens = stripped_line.split('|')

                node = tuple(map(int, tokens[0].split(','))) #Convert to numerical data
                self.bayesian_nodes[node] = float(tokens[1])
                

    def train(self, training_data):

        x = 1 / len(training_data)

        for training_data_row in training_data:
            
            if training_data_row in self.bayesian_nodes.keys():
                self.bayesian_nodes[training_data_row] += x
            else:
                self.bayesian_nodes[training_data_row] = x

    #Returns probability of the query being true provided some given evidence
    #Clarity should be a float between 0 - 1 representing how 'clear' the bayesian model is
    #When clarity is lower than 1, the model will include nodes that match that percentage or higher of givens into the calculations
    #The probability isn't exact but it can get close enough
    #Ideally, you should use a higher value like .75 or .9 and only when a large number of givens are present
    #The purpose behind the clarity value is to reduce overfitting of the model
    #A clarity of 1 means getting the probability the query matches a subset of the training data that matches a set of givens
    #Overfitting may not be a problem if theres a large enough amount of data
    def bayes_eval(self, query, givens, clarity=1):
        
        probability_of_query_given = 0
        probability_of_given = 0

        number_of_specified_givens = 0
        for g in givens:
            if g == None:
                continue
            number_of_specified_givens += 1

        for node in self.bayesian_nodes.keys():

            givens_true_for_node = 0
            for i in range(len(givens)):
                if givens[i] == None:
                    continue
                elif givens[i] == node[i]:
                    givens_true_for_node += 1

            givens_true_for_node /= number_of_specified_givens
            
            if givens_true_for_node >= clarity:
                probability_of_given += self.bayesian_nodes[node]
                query_true_for_node = True

                for j in range(len(query)):
                    if query[j] == None:
                        continue
                    elif query[j] != node[j]:
                        query_true_for_node = False
                        break
                
                if query_true_for_node:
                    probability_of_query_given += self.bayesian_nodes[node]

        return probability_of_query_given / probability_of_given
    
    def save(self, file_name):
        with open(file_name, 'w') as network_file:
            network_file.write(str(self))
    
    def __str__(self):

        result = ""

        for node in self.bayesian_nodes.keys():
            node_elements = []
            for item in node:
                node_elements.append(str(item))
            result += f"{','.join(node_elements)}|{self.bayesian_nodes[node]}\n"

        return result