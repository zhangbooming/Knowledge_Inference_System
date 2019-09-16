import unittest
import read, copy
from logical_classes import *
from kb_and_inference_engine import *
from game_masters import *

class KBTest(unittest.TestCase):
    # 就是这样看一看这个整体的结构是什么,该如何搞,这个是很重要的,就是检查嘛, 对于required的
    # 数组里面的所有的东西的哦,就是forbin的东西的哦,然后这里最最常用的就是parse_input的,
    # 如果是出的话,那么就好了, 说明正确的,然后,对于这个forbin如果出现在这个里面就是false,
    # 就是报错,这个都是前面已经写好的部分的了, 注意这个assert的用法和c++中是一致的,如果发现了
    # 这个是true的话,那就是毫无影响了,如果发现为false了,也是没有问题的,如果发现了不是我宣称的那样,
    # 那么就给你抛出异常的.

    def checkKb(self, kb, required, forbidden):
        for v in required:
            self.assertTrue(kb.kb_ask(parse_input(v)), \
                'Expected Fact cannot be found in KB: "%s"' % str(v))
        for v in forbidden:
            self.assertFalse(kb.kb_ask(parse_input(v)), \
                'Unexpected Fact found in KB: "%s"' % str(v))


    # 这个部分应该好好搞一下的哦,然后上面的就是事实的鉴定,接下来有了一个全新的这个movable的东西的
    # 这个才是重点的哦,然后,这里的你看看给的这个expected,moveable前面还是包上了这个fact的了,
    # 说明这个movalable, 也就是统一到这个事实之中去了,也是要和规则进行匹配之后,才能行得通的哦,
    # 这个步骤是必不可少的一步啊,如果不为空的话,如果expected的,也就是我这个movale来进行检测的了
    # 这个部分啊,就是如果为expected不为空的话,这个得到的movables,也就是如果是true的话, 那么就不用这样搞了
    # 如果为false的话,真正的强悍之处就来了,就是说明这个东西是空的,那还搞个什么啊, 如果不为空的话,
    # 那么直接往下去就可以的了,然后对这个expected里面的所有东西都是进行取值操作的,然后把这个东西
    # 解析出来看一看到底是不是在这个movables里面的哦, 如果再就算了,否则,就给你报错的哦,所以,现在基本上已经
    # 解决了这个困惑的哦,否则的话,我们就是发现expected是空的, 但是movale有东西,这样也是不行的是吧.
    # 基本上事实,和这个movable基本上搞清楚了,上面是事实的,但是,这个movable就是要靠这个游戏的类来实现的
    # 这个就是当前的现状的哦.
    def checkMovables(self, gm, expected):
        movables = gm.getMovables()
        if expected:
            self.assertTrue(movables, \
                'None of the expected Facts with MOVABLE predicate ' \
                'can be found: "%s"' % [str(x) for x in expected])
            for e in expected:
                self.assertTrue(parse_input(e).statement in movables,\
                    'Expected Fact with MOVABLE predicate '\
                    'cannot be found in KB: "%s"' % str(e))
        else:
            self.assertFalse(movables, \
                'Unexpecting Facts with MOVABLE predicate: %s'\
                    % [str(x) for x in movables])

    # 这里的直接生成这个这个游戏,但是所有的东西用的都是同一套系统的,就是如此的,
    # 先生成之后,然后去这个文件里面去读取东西,读取的原则,就是很简单的了,前面加了什么
    # 我就是直接读取进行生成的了,这里生成的就是一个游戏了.
    # 这个read的功能是在是强悍,然后直接弄完了这个游戏的类,所以,去看一看这个read是如何工作的哦.
    def test01(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_all_disks_on_peg_one.txt')
        expectedMovables = [
            'fact: (movable disk1 peg1 peg2)',
            'fact: (movable disk1 peg1 peg3)',
        ]
        self.checkMovables(th, expectedMovables)

    def test02(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_all_disks_on_peg_one.txt')
        required = [
            'fact: (on disk1 peg1)',
            'fact: (on disk2 peg1)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg1 peg1)',
            'fact: (movable disk2 peg1 peg2)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test03(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_two_smallest_on_peg_three.txt')
        expectedMovables = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
            'fact: (movable disk3 peg1 peg2)',
        ]
        self.checkMovables(th, expectedMovables)

    def test04(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_two_smallest_on_peg_three.txt')
        required = [
            'fact: (on disk1 peg3)',
            'fact: (on disk2 peg3)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg3 peg3)',
            'fact: (movable disk2 peg3 peg1)',
            'fact: (movable disk2 peg3 peg2)',
            'fact: (movable disk2 peg3 peg3)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg1)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk4 peg1 peg3)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test05(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_smallest_on_three_second_smallest_on_two.txt')
        expectedMovables = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
            'fact: (movable disk2 peg2 peg1)',
        ]
        self.checkMovables(th, expectedMovables)

    def test06(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_smallest_on_three_second_smallest_on_two.txt')
        required = [
            'fact: (on disk1 peg3)',
            'fact: (on disk2 peg2)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg3 peg3)',
            'fact: (movable disk2 peg2 peg2)',
            'fact: (movable disk2 peg2 peg3)',
            'fact: (movable disk3 peg1 peg1)',
            'fact: (movable disk3 peg1 peg2)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test07(self):
        th = Puzzle8Game()
        th.read('puzzle8_top_right_empty.txt')
        expectedMovables = [
            'fact: (movable tile4 pos2 pos1 pos3 pos1)',
            'fact: (movable tile8 pos3 pos2 pos3 pos1)',
        ]
        self.checkMovables(th, expectedMovables)

    def test08(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_top_right_empty.txt')
        required = []
        forbidden = [
            'fact: (movable tile1 pos1 pos1 pos1 pos1)',
            'fact: (movable tile1 pos2 pos2 pos2 pos2)',
            'fact: (movable tile1 pos2 pos2 pos2 pos1)',
            'fact: (movable tile1 pos2 pos2 pos1 pos2)',
            'fact: (movable tile1 pos2 pos2 pos2 pos3)',
            'fact: (movable tile1 pos2 pos2 pos3 pos2)',
            'fact: (movable tile1 pos2 pos2 pos1 pos1)',
            'fact: (movable tile1 pos2 pos2 pos3 pos1)',
            'fact: (movable tile1 pos2 pos2 pos1 pos3)',
            'fact: (movable tile1 pos2 pos2 pos3 pos3)',
            'fact: (movable tile5 pos1 pos1 pos3 pos1)',
            'fact: (movable tile5 pos1 pos1 pos3 pos3)',
        ]
        self.checkKb(p8.kb, required, forbidden)

    def test09(self):
        th = Puzzle8Game()
        th.read('puzzle8_center_empty.txt')
        expectedMovables = [
            'fact: (movable tile2 pos2 pos1 pos2 pos2)',
            'fact: (movable tile8 pos1 pos2 pos2 pos2)',
            'fact: (movable tile6 pos2 pos3 pos2 pos2)',
            'fact: (movable tile4 pos3 pos2 pos2 pos2)',
        ]
        self.checkMovables(th, expectedMovables)

    def test10(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_center_empty.txt')
        required = []
        forbidden = [
            'fact: (movable tile1 pos1 pos1 pos2 pos2)',
            'fact: (movable tile3 pos3 pos1 pos2 pos2)',
            'fact: (movable tile7 pos3 pos1 pos2 pos2)',
            'fact: (movable tile5 pos3 pos3 pos2 pos2)',
            'fact: (movable tile1 pos1 pos1 pos3 pos1)',
            'fact: (movable tile1 pos1 pos1 pos3 pos3)',
            'fact: (movable tile5 pos3 pos3 pos3 pos3)',
        ]
        self.checkKb(p8.kb, required, forbidden)


if __name__ == '__main__':
    unittest.main()
