from gameOfLife.cell import cell
from nose.tools import assert_equal
from nose.tools import with_setup

def test_does_cell_exist():
	"Does the cell object exist and instantiate properly?"
	testCell = cell(1,2,True)
	assert_equal(testCell.x, 1)
	assert_equal(testCell.y, 2)
	assert_equal(testCell.alive, True)

def test_cell_die():
	"Can the cell die?"
	testCell = cell(1,2,True)
	testCell.die()
	assert_equal(testCell.alive, False)

def test_cell_respawn():
	"Can the cell rise from the dead?"
	testCell = cell(1,2,True)
	testCell.respawn
	assert_equal(testCell.alive, True)

def test_is_alive():
	"Is the cell dead or alive?"
	testCell = cell(1,2,True)
	assert_equal(testCell.alive, True)
