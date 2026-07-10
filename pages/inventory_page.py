class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.sort = page.locator('[data-test="product-sort-container"]')
        self.badge = page.locator(".shopping_cart_badge")

    @staticmethod
    def _slug(item_name):
        return item_name.lower().replace(" ", "-")

    def add_to_cart(self, item_name):
        self.page.locator(f"#add-to-cart-{self._slug(item_name)}").click()

    def remove_from_cart(self, item_name):
        self.page.locator(f"#remove-{self._slug(item_name)}").click()

    def cart_badge_count(self):
        if self.badge.count() == 0:
            return 0
        return int(self.badge.text_content())

    def sort_by(self, option):
        # option: "az", "za", "lohi", "hilo"
        self.sort.select_option(option)

    def product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def product_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
