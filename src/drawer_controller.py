# File: src/drawer_controller.py

class DrawerController:
    def __init__(self):
        self.drawer_contents = []

    def add_item_to_drawer(self, item):
        self.drawer_contents.append(item)
        print(f"Added {item} to the drawer.")

    def remove_item_from_drawer(self, item):
        if item in self.drawer_contents:
            self.drawer_contents.remove(item)
            print(f"Removed {item} from the drawer.")
        else:
            print(f"{item} not found in the drawer.")

    def view_drawer_contents(self):
        if self.drawer_contents:
            print("Drawer contents:")
            for item in self.drawer_contents:
                print(f"- {item}")
        else:
            print("The drawer is empty.")

# Example usage:
if __name__ == "__main__":
    drawer = DrawerController()

    drawer.add_item_to_drawer("Socks")
    drawer.add_item_to_drawer("T-shirts")

    drawer.view_drawer_contents()

    drawer.remove_item_from_drawer("Socks")

    drawer.view_drawer_contents()
