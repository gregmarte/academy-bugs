import asyncio
from playwright.async_api import Page, expect
from pages.cart_page import CartPage

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    async def click_and_hold(self, selector: str, duration: float = 5.0):
        await self.page.dblclick(selector)
        await asyncio.sleep(2)
        await self.page.hover(selector)
        await self.page.mouse.down()
        await asyncio.sleep(duration)
        await self.page.mouse.up()

    async def click_hold_item_description(self):
        await expect(self.page.locator(".ec_details_description_content")).to_be_visible(timeout=30000)
        await self.page.click(".ec_details_description_content")
        await self.click_and_hold(".ec_details_description")

    async def verify_bug_popup(self, bug_count: int, type_of_bug: str, text_of_bug: str):
        await expect(self.page.get_by_role("heading", name="What did you find out?")).to_be_visible(timeout=30000)
        await self.page.locator(f'input[type="radio"][value="{type_of_bug}"]').check()
        await self.page.locator(f'input[type="radio"][value="{text_of_bug}"]').check()
        await self.page.get_by_role("button", name="Submit").click()
        await expect(self.page.get_by_text("Correct!")).to_be_visible()
        await self.page.locator("#view-report").click()

        match bug_count:
            case 1:
                bug_found_text = "#1 Awesome! You found a bug. Pretty easy right?"
            case 5:
                bug_found_text = "#5 Great job! You found 5 bugs already, having fun?"
            case _: 
                bug_found_text = f"You found {bug_count} bugs."
                                                                                                                          
        await expect(self.page.get_by_role("heading", name=bug_found_text)).to_be_visible(timeout=30000)    
        await self.page.get_by_role("button", name="Close").click()


    async def click_right_bar_ad_item_image(self):
        await self.page.click(".ec_product_image")   #Note: Bug 19 as per source code.
        
    async def click_spinner(self):
        await self.page.click(".ec_cart_billing_info_update_loader", force=True) 

    async def click_right_bar_ad_item_link(self):
        await self.page.click(".ec_product_title_link")

    async def click_manufacturer(self):
        await self.page.locator(".ec_details_manufacturer >> a").click()

    async def open_cart(self) -> CartPage: 
        await self.page.locator(".ec_cart_widget_button").hover()
        await self.page.locator(".ec_cart_widget_minicart_checkout_button").click()
        return CartPage(self.page)