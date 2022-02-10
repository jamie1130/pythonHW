import random
from functools import reduce
from utils import data_to_dictionary

class PageRankDiGraph(object):
    '''
    A simple class for representing directed links between states. 
    Constructs a dictionary of link for fast lookups from a list of input link tuples.
    '''
    def __init__(self, data):
        '''
        initialize with a dictionary representing links via data_to_dictionary()
        Args: 
            data: list of tuples
        Returns:
            None
        '''
        self.data = data
        self.link_dict = data_to_dictionary(data)
    
    def __len__(self):
        '''
        returns the number of edges in the graph as int
        '''
        return len(self.data) # I'm giving it to you- no need to change

    def get_nodes(self):
        '''
        returns a list of all nodes in the graph
        Args:
            None
        Returns:
            List of string (list of all nodes in the graph)
        '''
        # I'm giving it to you - no need to change or understand
        sung_to = reduce(lambda x, y: x+y, self.link_dict.values())
        singer = list(self.link_dict.keys())
        
        # easy trick to turn a list with duplicates items into list without duplicate items 
        return list(set(sung_to + singer)) 

    def __contains__(self, item):
        '''
        Running this function should give True if the item is present in the graph and False otherwise
        Args:
            item: string
        Returns:
            True if the item is present in the graph. False otherwise
        '''
        # hint: should be one line, consider using get_nodes
        return item in self.get_nodes()

    def __str__(self):
        '''
        Args:
            None
        Returns:
            "PageRankDiGraph with {number of nodes} nodes and {number of edges} edges."
            (Return the above string by replacing {number of nodes} and {number of edges} with actual values)
        '''
        return "PageRankDiGraph with {0} nodes and {1} edges.".format(len(self.get_nodes()), self.__len__())

    def __add__(self, other):
        '''
        Combines two PageRankDiGraphs
        Args:
            other: A different instance of this class
        Returns:
            new instance of PageRankDiGraph that contains both the edges of this instance and other
        '''
        # hint: should be one line
        return PageRankDiGraph(self.data + other.data)

    def linked_by(self, x):
        '''
        return a list of states linked from x, with states listed multiple times if they are linked multiple times.
        Args:
            x: string (a node of the graph)
        Returns:
            list of string (nodes connected to the input)
        '''
        # hint: should be one line
        return self.link_dict.get(x)

class PageRankIterator(object):
    """
    A custom iterator class for performing approximate PageRank 
    random walks through a PR_DiGraph. 
    """
    
    def __init__(self, graph, iteration_limit=20, jump_prob=0.85):
        '''
        When initialized, this class should create instance variables to store:
            - graph: the PageRankDiGraph instance, given as input
            - iteration_limit: an integer given as input,
            - jump_prob: a float between 0 and 1 (inclusive), given as input,
            - a counter 'iter': starting at 0, to log the number of steps taken,
            - current_state: variable whose value is one of the keys of the 'link_dict' of the 'PageRankDiGraph'. You can choose its initial value arbitrarily; in my code I chose 'self.current_state = "hamilton"'.
        Args:
            graph: instance of PageRankDiGraph class
            iteration_limit: integer (explained above)
            jump_prob: float (explained above)
        Returns:
            None
        '''
        self.graph = graph
        self.iteration_limit = iteration_limit
        self.jump_prob = jump_prob
        self.iter = 0
        self.current_state = "hamilton"
        if isinstance(graph, PageRankDiGraph) == False:
            raise TypeError("graph need to be an instance of PageRankDiGraph")

    def follow_link(self):
        '''
        Follow a random directed link in self.D. Teleports if either 
        the selected link links the state to itself, or 
        if there are no links from the current state.
        Args:
            None
        Returns:
            None
        '''
        
        try:    
            self.graph.__contains__(self.graph.linked_by(self.current_state))
            next_state = random.choice(self.graph.linked_by(self.current_state)) 
        except KeyError:
            self.teleport()
        if next_state == self.current_state:
            self.teleport()
        else:
            self.current_state = next_state
    
    def teleport(self):
        '''
        Set the current state to a state uniformly at random, 
        from the set of all possible states
        Args:
            None
        Returns:
            None
        '''
        # Hint: can be as short as one line, consider using one of the methods of PageRankDiGraph
        self.current_state = random.choice(self.graph.get_nodes())

    def __iter__(self):
        '''
        return the iterator object (self)
        '''
        return self

    def __next__(self):
        '''
        With probability self.p, follow the link   
        relationship; otherwise teleport, until the iteration_limit is reached.
        Args:
            None
        Returns:
            the iterator's current state
        '''     
        if self.iter < self.iteration_limit:
            if random.random() < self.jump_prob:
                self.follow_link()
            else:
                self.teleport()
            self.iter +=1
            return self.current_state
        else:
            raise StopIteration
            


# Implement class IterablePageRankDiGraph from scratch here!
class IterablePageRankDiGraph (PageRankDiGraph):
    
    def __init__(self, data, iteration_limit = 20, jump_prob = 0.75):
        super().__init__(data)
        self.iteration_limit = iteration_limit
        self.jump_prob = jump_prob
    
    def __str__():  
        return "IterablePageRankDiGraph with {0} nodes and {1} edges.".format(len(self.get_nodes()), self.__len__())
    
    def __iter__():
        return PageRankDiGraph(self)