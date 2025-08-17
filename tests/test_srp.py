
import sys
import os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.async_api import async_playwright
from pages.srp import SRPPage

async def run(playwright):
    browser = await playwright.firefox.launch(headless=False)
    page = await browser.new_page()
    srp_page = SRPPage(page)

    await srp_page.goto()
    await srp_page.click_close_cookies()
    await srp_page.click_filter_10_items()
    await srp_page.verify_bug_popup()
    await srp_page.check_item_crash()
    await srp_page.check_bug001_text()
    await srp_page.click_button_bug_report_submit()
    await srp_page.click_confirmation()
    await srp_page.click_view_report()
    await srp_page.verify_bug_found_first()
    await srp_page.click_close_report()
    await srp_page.verify_more_bugs()
    await srp_page.click_close_more_bugs()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())