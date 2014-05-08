from gameOfLife.cell import cell
from nose.tools import assert_equal
from nose.tools import with_setup

class cell_test():

	def setup(self):
		self.testCell = cell(1,2,True)

	def teardown(self):
		pass

	def test_does_cell_exist(self):
		"Does the cell object exist and instantiate properly?"
		assert_equal(self.testCell.x, 1)
		assert_equal(self.testCell.y, 2)
		assert_equal(self.testCell.current, True)
	
	def test_cell_die(self):
		"Can the cell die?"
		self.testCell.die()
		assert_equal(self.testCell.future, False)
	
	def test_cell_respawn(self):
		"Can the cell rise from the dead?"
		self.testCell.respawn
		assert_equal(self.testCell.future, True)
	
	def test_is_alive(self):
		"Is the cell dead or alive?"
		assert_equal(self.testCell.current, True)

	def test_change_states(self):
		"Can the cell change states"
		self.testCell.die()
		self.testCell.switch()
		assert_equal(self.testCell.current, self.testCell.future)
