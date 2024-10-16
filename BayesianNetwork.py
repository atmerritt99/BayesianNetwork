class BayesianNetwork:

    def __init__(self):
        self.bayesian_nodes = {}

    def train(self, training_data):

        x = 1 / len(training_data)

        for training_data_row in training_data:
            
            if training_data_row in self.bayesian_nodes.keys():
                self.bayesian_nodes[training_data_row] += x
            else:
                self.bayesian_nodes[training_data_row] = x

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