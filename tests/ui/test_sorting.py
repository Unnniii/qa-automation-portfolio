from pages.inventory_page import InventoryPage


def test_sort_price_low_to_high(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("lohi")
    prices = inv.product_prices()
    assert prices == sorted(prices)


def test_sort_name_a_to_z(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("az")
    names = inv.product_names()
    assert names == sorted(names)
