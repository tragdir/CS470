import random

class Node:

    name =""
    parentNames = []
    cpt = []

    def __init__(self, nodeInfo):
        """
        :param nodeInfo: in the format as [name, parents, cpt]
        """
        # name, parents, cpt

        self.name = nodeInfo[0]
        self.parentNames = nodeInfo[1].copy()
        self.cpt = nodeInfo[2].copy()


    def format_cpt(self):
        s_cpt = '\t'.join(self.parentNames) + '\n'
        for i in range(len(self.cpt)):
            s_cpt += bin(i).replace("0b", "").zfill(len(self.parentNames)).replace('0', 'T\t').replace('1', 'F\t')
            s_cpt += str(self.cpt[i]) + '\n'
        return s_cpt


    def print(self):
        print("name: {}\nparents:{}\ncpt:\n{}".format(self.name, self.parentNames, self.format_cpt()))


class BayesNet:
    nodes = []

    def __init__(self, nodeList):
        for n in nodeList:
            self.nodes.append(Node(n))

    def print(self):
        for n in self.nodes:
            n.print()



    def rejectionSampling(self, qVar, evidence, N):
        """
        :param qVar: query variable
        :param evidence: evidence variables and their values in a dictionary
        :param N: maximum number of iterations
        E.g. ['WetGrass',{'Sprinkler':True, 'Rain':False}, 10000]
        :return: probability distribution for the query
        """


        return []


    def  gibbsSampling(self, qVar, evidence, N):
        """
                :param qVar: query variable
                :param evidence: evidence variables and their values in a dictionary
                :param N: maximum number of iterations
                E.g. ['WetGrass',{'Sprinkler':True, 'Rain':False}, 10000]
                :return: probability distribution for the query
                """

        return []


# Sample Bayes net
nodes = [["Cloudy", [], [0.5]],
 ["Sprinkler", ["Cloudy"], [0.1, 0.5]],
 ["Rain", ["Cloudy"], [0.8, 0.2]],
 ["WetGrass", ["Sprinkler", "Rain"], [0.99, 0.9, 0.9, 0.0]]]
b = BayesNet(nodes)
b.print()

# Sample queries to test your code
# print(b.gibbsSampling("Rain", {"Sprinkler":True, "WetGrass" : False}, 100000))
# print(b.rejectionSampling("Rain", {"Sprinkler":True}, 1000))
