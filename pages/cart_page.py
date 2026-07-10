class CartPage:
    def __init__(self, page):
        self.page = page

    def items(self):
        return self.page.locator(".cart_item .inventory_item_name").all_text_contents()

    def remove(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f"#remove-{slug}").click()

    def go_to_checkout(self):
        self.page.locator("#checkout").click()
