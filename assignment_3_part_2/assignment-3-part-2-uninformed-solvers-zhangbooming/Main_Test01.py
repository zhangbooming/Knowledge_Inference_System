import unittest, inspect
from multiprocessing.pool import ThreadPool
from multiprocessing.context import TimeoutError
from student_code_game_masters import *
from student_code_uninformed_solvers import *
from student_code_uninformed_solvers_HanoiTower import *


class KBTest(unittest.TestCase):

    def setUp(self):
        self.pool = ThreadPool(processes=1)
        self.lastEndStep = 0

    def playXSteps(self, solver, plays):
        res = []
        for play in plays:
            x = play[0]
            while self.lastEndStep < x:
                solver.solveOneStep()
                self.lastEndStep += 1
            res.append(solver.gm.getGameState())
        return res

    def solve(self, solver):
        solver.solve()

    def runPlayXSteps(self, solver, plays, timeout=5):
        try:
            results = self.pool.apply_async(self.playXSteps, [solver, plays]).get(timeout)
            for index, play in enumerate(plays):
                expected = play[1]
                self.assertEqual(results[index], expected)
        except TimeoutError:
            raise Exception("Timed out: %s" % inspect.stack()[1][3])

    def runSolve(self, solver, timeout=5):

        try:
            self.pool.apply_async(self.solve, [solver,]).get(timeout)
            self.assertTrue(solver.gm.isWon())
        except TimeoutError:
            raise Exception("Timed out: %s" % inspect.stack()[1][3])

    def test06_GM_8Puzzle(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_top_right_empty.txt')
        required = [
            'fact: (movable tile6 pos3 pos2 pos3 pos3)',
            'fact: (movable tile8 pos2 pos3 pos3 pos3)',
        ]
        p8.setWinningCondition(required, 'puzzle8_all_forbidden.txt')
        self.assertFalse(p8.isWon())

        movables = p8.getMovables()
        self.assertEqual(p8.getGameState(), ((5, 4, -1), (6, 1, 8), (7, 3, 2)))
        print("movables[0]:::", (movables[0]))
        p8.makeMove(movables[0])
        self.assertEqual(p8.getGameState(), ((5,-1,4), (6,1,8), (7,3,2)))
        p8.reverseMove(movables[0])
        self.assertEqual(p8.getGameState(), ((5,4,-1),(6,1,8),(7,3,2)))

    def test08_BFS_8Puzzle(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_top_right_empty.txt')
        required = [
            'fact: (movable tile6 pos3 pos2 pos3 pos3)',
            'fact: (movable tile8 pos2 pos3 pos3 pos3)',
        ]
        p8.setWinningCondition(required, 'puzzle8_all_forbidden.txt')
        self.assertFalse(p8.isWon())

        solver = SolverBFS(p8,((1,2,3),(4,5,6),(7,8,-1)))

        self.runPlayXSteps(solver, [
            # [step, expected game state]
             [5, ((5, 4, 8), (6, -1, 1), (7, 3, 2))],
             [13, ((5, 4, 8), (-1, 6, 1), (7, 3, 2))],
             [21, ((6, 5, 4), (1, -1, 8), (7, 3, 2))]
        ])


    def test07_DFS_8Puzzle(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_top_right_empty.txt')
        required = [
            'fact: (movable tile6 pos3 pos2 pos3 pos3)',
            'fact: (movable tile8 pos2 pos3 pos3 pos3)',
        ]
        p8.setWinningCondition(required, 'puzzle8_all_forbidden.txt')
        self.assertFalse(p8.isWon())

        solver = SolverDFS(p8,((1,2,3),(4,5,6),(7,8,-1)))

        self.runPlayXSteps(solver, [
            # [step, expected game state]
            [9, ((5, 4, 3), (6, 1, -1), (7, 2, 8))],
            [17, ((5, -1, 4), (2, 1, 3), (6, 7, 8))],
            [34, ((5, 4, -1), (3, 2, 1), (6, 7, 8))],
        ])

    def test01_GM_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_3_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())
        th.getGameState()

        movables = th.getMovables()
        self.assertEqual(th.getGameState(), ((1,2,3),(),()))
        print(movables)
        th.makeMove(movables[0])
        self.assertEqual(th.getGameState(), ((2,3),(1,),()))
        th.reverseMove(movables[0])
        self.assertEqual(th.getGameState(), ((1,2,3),(),()))

    def test02_DFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_3_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverDFS_2(th,((),(),(1,2,3)))

        self.runPlayXSteps(solver, [
            # [step, expected game state]
            [3, ((3,), (2,), (1,))],
            [13, ((1,), (), (2, 3))],
            [22, ((), (), (1, 2, 3))],
        ])

    def test03_DFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_3_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverDFS_2(th, ((),(),(1,2,3)))
        self.runSolve(solver)

    def test04_BFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_3_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverBFS(th,((),(),(1,2,3)))

        self.runPlayXSteps(solver, [
            # [step, expected game state]
            [10, ((), (1, 2), (3,))],
            [11, ((1,), (3,), (2,))],
            [20, ((), (2, 3), (1,))],
        ])

    def test05_BFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_3_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverBFS(th, ((),(),(1,2,3)))
        self.runSolve(solver,)

    def test09_BFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_5_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverBFS(th, ((), (), (1, 2, 3, 4, 5)))
        self.runSolve(solver)

    def test10_DFS_Hanoi(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_5_all_disks_on_peg_one.txt')
        required = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
        ]
        th.setWinningCondition(required, 'hanoi_all_forbidden.txt')
        self.assertFalse(th.isWon())

        solver = SolverDFS(th, ((), (), (1, 2, 3, 4, 5)))
        self.runSolve(solver)