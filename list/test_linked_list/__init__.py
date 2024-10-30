import unittest
from linked_list import LinkedList

class TestLinkedListMethods(unittest.TestCase):

	def test_list(self):
		llist = LinkedList()
		self.assertEqual(llist.is_empty(), True)
		llist.add("First")
		self.assertEqual(llist.is_empty(), False)
		first = llist.delete_first()
		self.assertEqual(first, "First")

	def test_list_like_string(self):
		llist = LinkedList()
		for item in ("Item", "Item2", 34, "Item4"):
			llist.add(item)
		self.assertEqual(llist.__str__(), "List[Item4, 34, Item2, Item]")

	def test_find_method(self):
		llist = LinkedList()
		llist.add(1)
		llist.add("Just String")
		self.assertEqual(llist.is_empty(), False)
		self.assertEqual(llist.find(1), True)
		self.assertEqual(llist.find("Just String"), True)
		self.assertEqual(llist.find("Bad String"), False)

	def test_delete_method(self):
		llist = LinkedList()
		llist.add("Item")
		llist.add("Item2")
		llist.add("Item3")
		self.assertEqual(llist.__str__(), "List[Item3, Item2, Item]")
		self.assertEqual(llist.delete("Item2"), "Item2")
		self.assertEqual(llist.__str__(), "List[Item3, Item]")
		self.assertEqual(llist.delete("Item3"), "Item3")
		self.assertEqual(llist.__str__(), "List[Item]")
		self.assertEqual(llist.delete("Item"), "Item")
		self.assertEqual(llist.__str__(), "List[]")

		llist.add(123)
		llist.add(234)
		llist.add(234235)
		self.assertEqual(llist.delete(123), 123)
		self.assertEqual(llist.__str__(), "List[234235, 234]")
