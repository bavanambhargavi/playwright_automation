# import pytest
# from playwright.sync_api import sync_playwright, Playwright, Page


# @pytest.fixture()
# def page(page: Page):
#     with sync_playwright() as p:
#         # browser = p.chromium.launch(headless=False, slowmo=2000)
#         browser = p.chromium.launch(headless=False, slow_mo=8)
#         page = browser.new_page()

#         # page.goto("/")
#         yield page

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }








