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
    def get_probability(self, query, givens):
        
        probability_of_query_given = 0
        probability_of_given = 0

        for node in self.bayesian_nodes.keys():

            givens_true_for_node = True
            for i in range(len(givens)):
                if givens[i] == None:
                    continue
                elif givens[i] != node[i]:
                    givens_true_for_node = False
                    break
            
            if givens_true_for_node:
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