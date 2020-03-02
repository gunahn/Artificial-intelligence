# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    nderstand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    from util import Stack
    from game import Directions

    Destination = Stack()
    VisitedNode = []
    Path = []

    if problem.isGoalState(problem.getStartState()):
        return []

    Destination.push((problem.getStartState(), []))

    print("Destination:" ,Destination)

    while not Destination.isEmpty():
        Node, Path = Destination.pop()
        #print("Node:", Node)
        #print("Path: ", Path)
        if problem.isGoalState(Node):
            return Path
        if Node not in VisitedNode:
            successor = problem.getSuccessors(Node)
            VisitedNode.append(Node)
            for location, action, cost in successor:
                if location not in VisitedNode:
                    Destination.push((location, Path+[action]))

    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    from game import Directions
    Destination = Queue()

    VisitedNode =[]
    Path=[]
    if problem.isGoalState(problem.getStartState()):
        return []

    Destination.push((problem.getStartState(),[]))

    while not Destination.isEmpty():
        Node, Path = Destination.pop()

        if problem.isGoalState(Node):
            return Path
        if Node not in VisitedNode:
            Successor = problem.getSuccessors(Node)

            VisitedNode.append(Node)
            for location, action, cost in Successor:
                if (location not in VisitedNode):
                    Destination.push((location, Path + [action]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    from util import PriorityQueue
    Destination = PriorityQueue()
    VisitedNode = set()
    Path = []
    distance = {}

    if problem.isGoalState(problem.getStartState()):
        return []

    Destination.push((problem.getStartState(), []), 0)
    distance[problem.getStartState()] = 0
    while not Destination.isEmpty():
        Node, Path = Destination.pop()
        if Node in VisitedNode:
            continue
        VisitedNode.add(Node)
        pathCost = distance[Node]
        if problem.isGoalState(Node):
            return Path
        successors = problem.getSuccessors(Node)
        for successor in successors:
            location, action, cost = successor[0], successor[1], successor[2]
            if location in distance and distance[location] <= pathCost + cost:
                continue
            elif location in distance:
                Destination.update((location, Path + [action]), pathCost + cost)
            else:
                Destination.push((location, Path + [action]), pathCost + cost)
            distance[location] = pathCost + cost

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    Destination = PriorityQueue()
    VisitedNode = []
    Path = []

    if problem.isGoalState(problem.getStartState()):
        return []

    Destination.push((problem.getStartState(),Path),0)
    while Destination:
        Node, Path = Destination.pop()
        if problem.isGoalState(Node):
            break
        if Node not in VisitedNode:
            VisitedNode.append(Node)
            Successor = problem.getSuccessors(Node)
            for location, action, cost in Successor:
                NextCost = problem.getCostOfActions((Path+[action]))+ heuristic(location,problem)
                if location not in VisitedNode:
                    Destination.push((location, (Path+[action])), NextCost)
    return Path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
