from playwright.sync_api import sync_playwright
# from playwright.sync_api import Page
import time


def test_record():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="record_video/",
            record_video_size={"width": 400, "height": 400}
        )
        page = context.new_page()
        page.goto("http://www.google.com/")
        time.sleep(2)
        page.get_by_title("Search").fill("Apple")
        page.keyboard.press("Enter")
        time.sleep(2)
        page.locator(
            "//span[normalize-space()='Apple - Official Site']").click()
        time.sleep(3)
        page.get_by_role("link", name="iphone").first.click()
        time.sleep(4)
        a = page.locator("span.chapternav-label").all()
        a[2].click()
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
        page.locator("#applecareplus_59_noapplecare_label").click()
        time.sleep(5)
        page.get_by_role("button", name="Add to Bag").click()
        time.sleep(2)
        page.get_by_role("button", name="Review Bag").click()
        time.sleep(4)
        context.close()
        page.close()
