from pages.inventory_page import InventoryPage


def test_add_to_cart_updates_badge(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("Sauce Labs Backpack")
    assert inv.cart_badge_count() == 1


def test_remove_from_cart_decrements(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("Sauce Labs Backpack")
    inv.add_to_cart("Sauce Labs Bike Light")
    assert inv.cart_badge_count() == 2
    inv.remove_from_cart("Sauce Labs Backpack")
    assert inv.cart_badge_count() == 1
