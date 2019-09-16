import unittest
import student_code

class SetupTest(unittest.TestCase):

	def test01(self):
		result = student_code.shouldReturnTrue()
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()
