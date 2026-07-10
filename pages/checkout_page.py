class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_details(self, first, last, zip_code):
        self.page.locator("#first-name").fill(first)
        self.page.locator("#last-name").fill(last)
        self.page.locator("#postal-code").fill(zip_code)
        self.page.locator("#continue").click()

    def item_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def item_total(self):
        # "Item total: $39.98"
        text = self.page.locator(".summary_subtotal_label").text_content()
        return float(text.split("$")[1])

    def finish(self):
        self.page.locator("#finish").click()

    def confirmation_message(self):
        return self.page.locator(".complete-header").text_content()
