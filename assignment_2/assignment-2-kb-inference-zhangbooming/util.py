import logical_classes as lc

def is_var(var):
    """Check whether an element is a variable (either instance of Variable, 
        instance of Term (where .term is a Variable) or a string starting with 
        `'?'`, e.g. `'?d'`)

    Args:
        var (any): value to check

    Returns:
        bool
    """
# 这里面没有rule的任何东西,仅仅有fact的对比的关系的,感觉这一次是硬仗的,这个is_var就很有帮助的
# 因为rule的定义是什么,要去看一看的,如果是str的东西,就是返回问号的, 如果是这个term里面的,
# 这个term里面,然后这个变量的,

    if type(var) == str:
        return var[0] == "?"
    if isinstance(var, lc.Term):
        return isinstance(var.term, lc.Variable)

    return isinstance(var, lc.Variable)

def match(state1, state2, bindings=None):
    """Match two statements and return the associated bindings or False if there
        is no binding

    Args:
        state1 (Statement): statement to match with state2
        state2 (Statement): statement to match with state1
        bindings (Bindings|None): already associated bindings

    Returns:
        Bindings|False: either associated bindings or no match found
    """
    if len(state1.terms) != len(state2.terms) or state1.predicate != state2.predicate:
        return False
    if not bindings:
        bindings = lc.Bindings()
    return match_recursive(state1.terms, state2.terms, bindings)

def match_recursive(terms1, terms2, bindings):  # recursive...
    """Recursive helper for match

    Args:
        terms1 (listof Term): terms to match with terms2
        terms2 (listof Term): terms to match with terms1
        bindings (Bindings): already associated bindings

    Returns:
        Bindings|False: either associated bindings or no match found
    """
# 这个部分要小心的,  就是我最后还是要参考这个来写自己的匹配的函数的, 这个涉及到了一个大的rule的
# 问题,这个真的是要小心搞一搞的,

    if len(terms1) == 0:
        return bindings
    if is_var(terms1[0]):
        if not bindings.test_and_bind(terms1[0], terms2[0]):
            return False
    elif is_var(terms2[0]):
        if not bindings.test_and_bind(terms2[0], terms1[0]):
            return False
    elif terms1[0] != terms2[0]:
        return False
    return match_recursive(terms1[1:], terms2[1:], bindings)

def instantiate(statement, bindings):
    """Generate Statement from given statement and bindings. Constructed statement
        has bound values for variables if they exist in bindings.

    Args:
        statement (Statement): statement to generate new statement from
        bindings (Bindings): bindings to substitute into statement
    """
# 这个是定义一个部分的,如果,是term的话,我们就返回什么的,否则,就返回什么的,然后又是一个弄完的
# 不懂的地方是在太多了, 实例化一个东西的,bound, 这里是递归,自己调用自己, 这个函数是很难写的,
# 我赌,一定会用到这个函数的,


    def handle_term(term):
        if is_var(term):
            bound_value = bindings.bound_to(term.term)
            return lc.Term(bound_value) if bound_value else term
        else:
            return term

    new_terms = [handle_term(t) for t in statement.terms]
    return lc.Statement([statement.predicate] + new_terms)

def factq(element):
    """Check if element is a fact

    Args:
        element (any): element to check


    Returns:
        bool
    """
    return isinstance(element, lc.Fact)

def printv(message, level, verbose, data=[]):
    """Prints given message formatted with data if passed in verbose flag is greater than level

    Args:
        message (str): message to print, if format string data should have values
            to format with
        level (int): value of verbose required to print
        verbose (int): value of verbose flag
        data (listof any): optional data to format message with
    """
    if verbose > level:
        print(message.format(*data) if data else message)