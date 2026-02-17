from playwright.sync_api import Page

class LoginPlayground:

    def __init__(self,page:Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/sampleapp")
        self.username_inp=self.page.get_by_placeholder("User Name")
        self.password_inp=self.page.get_by_placeholder("********")
        self.login_btn=self.page.get_by_role("button",name="Log In")
        self.label_val=self.page.locator("label#loginstatus")

    def Login(self,username,password):
        self.username_inp.fill(username)
        self.password_inp.fill(password)
        self.login_btn.click()
