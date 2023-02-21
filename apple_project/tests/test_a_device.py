from playwright.sync_api import Page
import time


def test_run(playwright, page):
    iphone_13 = playwright.devices["iPhone 11"]
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
       **iphone_13
       )
    page = context.new_page()
    page.goto("http://www.google.com")
    time.sleep(10)
    page.get_by_role("textbox").fill("Apple")
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator(
            "//span[normalize-space()='Apple - Official Site']").click()
    time.sleep(3)
    page.get_by_role("link", name="iphone").first.click()
    time.sleep(4)
#     a = page.locator("span.chapternav-label").all()
#     a[2].click()
    page.locator("//span[@class='chapternav-label'][normalize-space()='iPhone 13']").click()
    
    time.sleep(2)
    s = page.locator("span.row").all()
    s[1].click()
    time.sleep(4)
    k = page.locator("img.colornav-swatch").all()
    k[3].click()
    time.sleep(3)
    k = page.locator("span.row").all()
    k[4].click()
    time.sleep(2)
    page.get_by_text("No trade-in").click()
    time.sleep(3)
    page.locator("#applecareplus_59_noapplecare_label").click()
    time.sleep(5)
    # page.click('button:text("Add to Bag")')
    # time.sleep(4)
    page.get_by_role("button", name="Add to Bag").click()
    time.sleep(2)
    page.get_by_role("button", name="Review Bag").click()
    time.sleep(4)
    page.close()
    browser.close()
    context.close()
