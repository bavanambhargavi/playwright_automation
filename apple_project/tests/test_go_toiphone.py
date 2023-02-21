from playwright.sync_api import sync_playwright
import time


def test_gotoiphone(page):
    page.goto("http://www.google.com/")
    time.sleep(2)
    page.get_by_title("Search").fill("Apple")
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator("//span[normalize-space()='Apple - Official Site']").click()
    time.sleep(3)
    page.get_by_role("link", name="iphone").first.click()
    time.sleep(4)
    page.screenshot(path="..//data//screenshots//apple2.png")
    page.close()
