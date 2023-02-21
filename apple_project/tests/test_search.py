import time
from playwright.sync_api import Playwright


def test_openbrowser(page):
    page.goto("http://www.google.com/")
    time.sleep(2)
    page.get_by_title("Search").fill("Apple")
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator("//span[normalize-space()='Apple - Official Site']").click()
    time.sleep(3)
    # page.screenshot(path="")
    page.screenshot(path="apple1.png", full_page=True)
    page.close()
