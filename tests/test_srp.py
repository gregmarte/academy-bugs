
import sys
import os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.async_api import async_playwright
from pages.srp import SRPPage
from pages.product_page import ProductPage

browser = None
bug_count:int = 0

async def open_srp_cookies(srp_page: SRPPage):
    await srp_page.goto()
    await srp_page.click_close_cookies()
    
async def bug001_item_filter(srp_page: SRPPage):
    global bug_count
    await srp_page.click_filter_10_items()
    bug_count += 1
    await srp_page.verify_bug1_popup()
    await srp_page.check_item_crash()
    await srp_page.check_bug001_text()
    await srp_page.click_button_bug_report_submit()
    await srp_page.click_confirmation()
    await srp_page.click_view_report()
    await srp_page.verify_bug_found_first()
    await srp_page.click_close_report()

async def bug002_srp_item_spacing(srp_page: SRPPage):
    #pre-confidion, on the SRP
    #post-condition, one more bug found, still on SRP
    global bug_count
    await srp_page.click_item(2)
    bug_count += 1
    await srp_page.verify_bug_popup(bug_count, "Visual", "The product image fills the box entirely just like all other product images" )
    return await srp_page.post_click_item()

async def bug010_product_description(product_page: ProductPage):
    # pre-condition, on the SRP page
    global bug_count
    
    await product_page.click_hold_item_description()
    bug_count += 1
    await product_page.verify_bug_popup(bug_count, "Content", "The text should be in English language")

async def main():
    async with async_playwright() as playwright:
        global browser
        browser = await playwright.firefox.launch(headless=False)
        page = await browser.new_page()
        active_page = SRPPage(page)
        product_page = ProductPage(page)
        
        await open_srp_cookies(active_page)
        await bug001_item_filter(active_page)
        product_page = await bug002_srp_item_spacing(active_page)
        await bug010_product_description(product_page)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())