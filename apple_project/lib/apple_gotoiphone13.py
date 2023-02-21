# from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import time


def test_gotoiphone(page: Page):
    page.goto("http://www.google.com/")
    time.sleep(2)
    page.get_by_title("Search").fill("Apple")
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator("//span[normalize-space()='Apple - Official Site']").click()
    time.sleep(3)
    page.get_by_role("link", name="iphone").first.click()
    time.sleep(4)
    page.locator(
        "//span[@class='chapternav-label'][normalize-space()='iPhone 13']").click()
    time.sleep(5)
    page.screenshot(path="..//data//screenshots//apple3.png")
    page.close()
