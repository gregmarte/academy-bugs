import asyncio
from playwright.async_api import Page, expect

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

    async def verify_bug002_popup(self, bug_count: int):
        await expect(self.page.get_by_role("heading", name="What did you find out?")).to_be_visible(timeout=30000)
        await self.page.locator('input[type="radio"][value="Content"]').check()
        await self.page.locator('input[type="radio"][value="The text should be in English language"]').check()
        await self.page.get_by_role("button", name="Submit").click()
        await expect(self.page.get_by_text("Correct!")).to_be_visible()
        await self.page.locator("#view-report").click()

        if bug_count == 1:
            bug_found_text = "#1 Awesome! You found a bug. Pretty easy right?"
            more_bugs_text = "There are more bugs in the product details page, please keep searching. Additionally: Check a product with color options."
        else:
            bug_found_text = f"You found {bug_count} bugs."
            more_bugs_text = "There are more bugs in the product details page, please keep searching. Additionally: Check a product with color options."
                                                                                                                          
        await expect(self.page.get_by_role("heading", name=bug_found_text)).to_be_visible(timeout=30000)    
        await self.page.get_by_role("button", name="Close").click()
 
        await expect(self.page.get_by_text(more_bugs_text)).to_be_visible(timeout=10000)
        await self.page.get_by_role("button", name="Close").click()
