from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### student code goes here
        ### pass
        list1 = self.search("peg1")
        list2 = self.search("peg2")
        list3 = self.search("peg3")
        tup = (tuple(list1), tuple(list2), tuple(list3))
        # print("tup::", tup)
        return tup

    def search(self, peg):
        # print("peg::", peg)
        list = []
        bindings_lst = self.kb.kb_ask(Fact(("on ?x "+peg).split()))
        if bindings_lst == False:
            pass
            # print("list::", list)
            # print("查询peg结果为False,结束!!")
        else:
            for bindings_ in bindings_lst:
                str = bindings_.bindings[0].constant.element
                # print("str::", str)
                num = int(str[-1])
                list.append(num)
                # print("num::", num)
            # num1 = bindings_lst[0].bindings[0].constant.element
            list.sort()
            # print("list::", list)
        return list

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        ### pass
        pred = movable_statement.predicate
        sl = movable_statement.terms

        list2 = self.search(sl[2].__str__())
        if(list2.__len__() == 0):
            self.kb.kb_retract(Fact(["EMPTY", sl[2]]))
            self.kb.kb_assert(Fact(["on", sl[0], sl[2]]))
            self.kb.kb_assert(Fact(["TOP", sl[0], sl[2]]))
        else:
            oldTop = "disk"+str(list2[0])
            self.kb.kb_retract(Fact(["TOP", oldTop, sl[2]]))
            self.kb.kb_assert(Fact(["TOP", sl[0], sl[2]]))
            self.kb.kb_assert(Fact(["on", sl[0], sl[2]]))

        list1 = self.search(sl[1].__str__())
        if(list1.__len__() == 1):
            self.kb.kb_retract(Fact(["on", sl[0], sl[1]]))
            self.kb.kb_retract(Fact(["TOP", sl[0], sl[1]]))
            self.kb.kb_assert(Fact(["EMPTY", sl[1]]))
        else:
            secondTop = "disk"+str(list1[1])
            self.kb.kb_retract(Fact(["on", sl[0], sl[1]]))
            self.kb.kb_retract(Fact(["TOP", sl[0], sl[1]]))
            self.kb.kb_assert(Fact(["TOP", secondTop, sl[1]]))

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        ##pass

        # fact = Fact("coordinate ?x pos1 pos1")
        # bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos1 pos1".split()))
        # num1 = bindings_lst[0].bindings[0].constant
        # print("Fact::::", fact)
        # print("Fact.statement::::", fact.statement)
        # print("isinstance(fact, Fact)", isinstance(fact, Fact))
        # print("binding_lst::::", bindings_lst)
        # print("bindings_lst[0][0]:::::", bindings_lst[0].bindings[0].constant)

        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos1 pos1".split()))
        num1 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos2 pos1".split()))
        num2 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos3 pos1".split()))
        num3 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos1 pos2".split()))
        num4 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos2 pos2".split()))
        num5 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos3 pos2".split()))
        num6 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos1 pos3".split()))
        num7 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos2 pos3".split()))
        num8 = bindings_lst[0].bindings[0].constant.element
        bindings_lst = self.kb.kb_ask(Fact("coordinate ?x pos3 pos3".split()))
        num9 = bindings_lst[0].bindings[0].constant.element
        tup = ((int(num1), int(num2), int(num3)),
                (int(num4), int(num5), int(num6)),
                (int(num7), int(num8), int(num9)))
        # print("num1:::", type(num1))
        # tup = (int(num1), int(num2), int(num3))
        # print("tup:::", tup)
        return tup



    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        ### pass
        pred = movable_statement.predicate
        sl = movable_statement.terms
        oldList1 = ["coordinate", sl[0], sl[1], sl[2]]
        oldList2 = ["coordinate", '-1', sl[3], sl[4]]
        oldFact1 = Fact(Statement(oldList1))
        oldFact2 = Fact(Statement(oldList2))
        # fact1 = self.kb._get_fact(tileFact)
        # fact2 = self.kb._get_fact(emptyFact)
        # print("fact1:::   ", fact1)
        # print("fact2:::   ", fact2)
        self.kb.kb_retract(oldFact1)
        self.kb.kb_retract(oldFact2)
        newFact1 = Fact(["coordinate", sl[0], sl[3], sl[4]])
        newFact2 = Fact(["coordinate", '-1', sl[1], sl[2]])
        self.kb.kb_assert(newFact1)
        self.kb.kb_assert(newFact2)




    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
