class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.submit = page.locator("#login-button")
        self.error = page.locator('[data-test="error"]')

    def load(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def error_message(self):
        return self.error.text_content()
