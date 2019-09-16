import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if isinstance(fact, Fact):
            if fact not in self.facts:
                self.facts.append(fact)

        print("Asserting {!r}".format(fact))


    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """

        answers = ListOfBindings()
        for i in range(len(self.facts)):
            result = match(fact.statement, self.facts[i].statement)
            if result != False:
                answers.add_bindings(result)
        if len(answers) == 0:
            return False
        else:
            return answers

        print("Asking {!r}".format(fact))


