import unittest
from PotatoArray import PotatoArray

class MyTestCase(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.a = PotatoArray([1, 2, 3])
		self.b = PotatoArray([2, 3, 4, 5, 6, 7, 8, 9, 10])

	def test_index_0(self):
		with self.assertRaises(IndexError):
			self.a[0]
		with self.assertRaises(IndexError):
			self.b[0]


	def test_index_1(self):
		with self.assertRaises(IndexError):
			self.a[1]
		with self.assertRaises(IndexError):
			self.b[1]

	def test_index_neg1(self):
		with self.assertRaises(IndexError):
			self.a[-1]
		with self.assertRaises(IndexError):
			self.b[-1]

	def test_index_2(self):
		self.assertEqual(self.a[2], 1)
		self.assertEqual(self.b[2], 2)

	def test_index_neg2(self):
		self.assertEqual(self.a[-2], 3)
		self.assertEqual(self.b[-2], 10)

	def test_add(self):
		c = self.a + self.b
		self.assertEqual(len(c), len(self.a) + len(self.b))
		self.assertEqual(c[2], 1)
		self.assertEqual(c[-2], 10)
		self.assertEqual(c[5], 2)

	def test_copy(self):
		c = self.a.copy()
		self.assertEqual(len(c), len(self.a))
		self.assertEqual(c[2], 1)
		self.assertEqual(c[4], 3)
		self.assertFalse(self.a is c)

	def test_eq(self):
		self.assertEqual(PotatoArray([1,2,3]), self.a)
		self.assertNotEqual(self.a, self.b)

if __name__ == '__main__':
	unittest.main()


