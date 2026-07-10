from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_e2e(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("Sauce Labs Backpack")
    inv.add_to_cart("Sauce Labs Bike Light")
    inv.go_to_cart()

    cart = CartPage(logged_in_page)
    assert len(cart.items()) == 2
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_details("Jane", "Doe", "12345")
    # the headline assertion: displayed subtotal equals the summed item prices
    assert checkout.item_total() == round(sum(checkout.item_prices()), 2)
    checkout.finish()
    assert "Thank you for your order" in checkout.confirmation_message()
