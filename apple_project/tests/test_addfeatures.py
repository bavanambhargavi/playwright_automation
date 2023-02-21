# import pytest
from playwright.sync_api import sync_playwright
import time


def test_addfeatures(page):
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
    s = page.locator("span.row").all()
    s[1].click()
    time.sleep(4)
    k = page.locator("img.colornav-swatch").all()
    k[3].click()
    time.sleep(3)
    k = page.locator("span.row").all()
    k[4].click()
    time.sleep(2)
    page.screenshot(path="..//data//screenshots//apple4.png")
    page.close()
