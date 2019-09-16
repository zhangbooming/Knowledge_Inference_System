from logical_classes import *
from kb_and_inference_engine import *
from read import *
from abc import ABC, abstractmethod
import os

# 这个才是真正的游戏监控的类,我们有了这个kb,这个是不进行什么修改的,但是这个game却是要严格
# 来监控这个movale的活动的,你看看这个kb. 这个包含fact和rule的东西也只是我们游戏类的一部分,
# 我们可以设想这个仅仅就是这个内部的存储,这个moveable到底应该放在哪里的呢, 结果还是和事实放在一起的
# 毕竟我们之前看过了,因为这个规范不允许我们单独放开,否则,不在一个整体内是如何来搞的呢,所以,movable
# 还是要放在这个规则里面的哦,也就是kb里面的,只是一种事实而已的,来来来,看看这个movable到底有没有
# 这个东西的哦, 这个是很神奇的东西的哦,初始化这个之后,弄出一个新的kb的,然后弄出了这个movaeb查询的东西的
# 一个抽象的方法进行冲洗的,这个抽象的查询方法到底应该怎么放进去的呢,对对对,这是很多个游戏的通用的方法
# 这个moveable其实就是facts中的一种的, 所以,我们只是查询出来而已的,只是这里的执行的开头是moveable
# 而已的哦,

class GameMaster(ABC):

    TXTS_DIRECTORY_PATH='flatfiles'

    def __init__(self):
        self.kb = KnowledgeBase([], [])
        self.moveableQuery = self.produceMovableQuery()

    @abstractmethod
    def produceMovableQuery(self):
        raise NotImplementedError('Subclasses must override produceMovableQuery() '\
            'to provide the query for facts starting with MOVABLE predicate')

    # 这个只是把这个kb进行了一点包装而已,以前的kb还是以前的kb,并没有做什么新的工作的哦,其实就是
    # 这样的一个样子的哦,然后就是开始探寻的哦,把这个东西问一下,注意问的是一个变量的,所以,这个绑定是非常之多的
    # 然后,这个ask的绑定就可以告知了一定的结果,目前就是这样的一个样子的哦,告知了这个结果之后的呢,
    # 就是接下里很简单的办法的了,然后,问了这个之后的呢,然后,这里面有很多个板顶,然后,将这个绑定一个个实例化
    # 以后,弄好成这个Fact的事实给返回回去,其实就是这样的一个道理,没有什么其他的神奇的地方的哦,
    # 还有这个类有毒东西的方法, 哈哈哈哈,这个读写的方法,将这个read的文件里的方法给拷贝过来,形成了
    # 一种封装的,也就是要完全封装好的哦, 其实这个部分就已经就是尽可能包装了一个很是一层的东西的
    # 然后就是连接这个路径,然后, 读取这个文件,然后,把里面的东西都给弄出来的, 包括这个rule和fact,
    # 但是,题目上没有给出rule的具体规则,也没有给出具体写法,我觉得,老师应该会给出rule的,这里都是
    # fact, 所以,我们只要按照规矩吧这个fact给写上去其实也就是可以了,不需要考虑其他的东西的了,
    # 就是这样的一个过程的哦,没有什么了,当然main里面有东西,直接复制粘贴一份其实也就可以的了.

    def getMovables(self):        
        listOfBindings = self.kb.kb_ask(self.moveableQuery)
        if listOfBindings:
            return [instantiate(self.moveableQuery.statement,bindings)\
                     for bindings in listOfBindings]
        else:
            return listOfBindings

    def read(self, file_name, path=TXTS_DIRECTORY_PATH):
        final_path = os.path.join(path, file_name)
        for fr in read_tokenize(final_path):
            self.kb.kb_assert(fr)

# 我就是是说嘛,这个就是解析的是这个返回的是一个按照一定格式的moveable,这个就是一个事实而已的哦
# 其他的就是这样的一个样子的哦, 然后,就是继续往前就是, 这个就是解析之后,就是形成了一个形参的东西,
# 也就是一大堆varaible的东西,所以,,并且长度要合适的, 这里就是唯一的一种东西的了, 因为以这个开头的就是
# 同样参数的字符串给过去的哦,初始化的时候,已经是创造好的了.

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        return parse_input('fact: (movable ?disk ?init ?target)')

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')


