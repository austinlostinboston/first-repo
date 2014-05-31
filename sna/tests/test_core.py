import unittest
from SNA.sna.core import *

class TestCore(unittest.TestCase):

	def setUp(self):
		self.graph1 = [[1,2],[2,3],[3,1]]
		self.graph2 = [[1,2],[2,3],[3,4],[4,5],[5,1],[2,5]]

	def test_nodes(self):
		self.assertEqual(nodes(self.graph1),[1,2,3])

	def test_n_nodes(self):
		self.assertEqual(n_nodes(self.graph1),3)

	def test_n_edges(self):
		self.assertEqual(n_edges(self.graph2),6)

	def test_nodes_edges(self):
		self.assertEqual(nodes_edges(3,self.graph2),[[2,3],[3,4]])

	def test_total_deg(self):
		self.assertEqual(total_deg(5,self.graph2),3)

	def test_in_edges(self):
		self.assertEqual(in_edges(5,self.graph2),[[4,5],[2,5]])

	def test_in_degree(self):
		self.assertEqual(in_degree(5,self.graph2),2)

	def test_out_edges(self):
		self.assertEqual(out_edges(2,self.graph2),[[2,3],[2,5]])

	def test_out_degree(self):
		self.assertEqual(out_degree(2,self.graph2),2)

if __name__ == '__main__':
	unitest.main()