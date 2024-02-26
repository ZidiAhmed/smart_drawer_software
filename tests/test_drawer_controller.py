# File: tests/test_drawer_controller.py
import unittest
from src.drawer_controller import DrawerController

class TestDrawerController(unittest.TestCase):
    def setUp(self):
        # Create a new DrawerController instance for each test
        self.drawer = DrawerController()

    def test_add_item_to_drawer(self):
        self.drawer.add_item_to_drawer("Socks")
        self.assertIn("Socks", self.drawer.drawer_contents)

    def test_remove_item_from_drawer(self):
        self.drawer.add_item_to_drawer("T-shirts")
        self.drawer.remove_item_from_drawer("T-shirts")
        self.assertNotIn("T-shirts", self.drawer.drawer_contents)

    def test_remove_nonexistent_item(self):
        result = self.drawer.remove_item_from_drawer("Nonexistent Item")
        self.assertEqual(result, None)
        self.assertNotIn("Nonexistent Item", self.drawer.drawer_contents)

    def test_view_drawer_contents_empty(self):
        with self.assertLogs() as cm:
            self.drawer.view_drawer_contents()

        self.assertEqual(len(cm.output), 1)
        self.assertIn("The drawer is empty.", cm.output[0])

    def test_view_drawer_contents_nonempty(self):
        self.drawer.add_item_to_drawer("Socks")
        with self.assertLogs() as cm:
            self.drawer.view_drawer_contents()

        self.assertEqual(len(cm.output), 2)
        self.assertIn("Drawer contents:", cm.output[0])
        self.assertIn("- Socks", cm.output[1])

if __name__ == '__main__':
    unittest.main()
