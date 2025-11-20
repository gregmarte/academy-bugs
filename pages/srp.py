from playwright.async_api import Page, expect
from pages.product_page import ProductPage

class SRPPage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self):
        await self.page.goto("https://academybugs.com/find-bugs")

    async def click_close_cookies(self):
        await self.page.get_by_text("Functional only").click()

    async def click_filter_10_items(self):
        await self.page.locator("a.what-we-offer-pagination-link:nth-child(2)").click()

    async def verify_bug1_popup(self):
        await expect(self.page.get_by_text("What did you find out?")).to_be_visible(timeout=60000)

    async def check_item_crash(self):
        await self.page.locator('input[type="radio"][value="Crash"]').check()

    async def check_item_visual(self):
        await self.page.locator('input[type="radio"][value="Visual"]').check()

    async def click_item(self, item_number: int):
        xpath_expression = f'(//li[@class="ec_product_li"])[{item_number}]'
        await self.page.locator(xpath_expression).click()

    async def post_click_item(self):
        return ProductPage(self.page)
        
    async def check_bug001_text(self):
        await self.page.locator('input[type="radio"][value="The selected number of results is displayed according to the clicked buttons"]').check()

    async def check_bug002_text(self):
        await self.page.locator('input[type="radio"][value="The product image fills the box entirely just like all other product images"]').check()

    async def click_button_bug_report_submit(self):
        await self.page.get_by_role("button", name="Submit").click()

    async def click_confirmation(self):
        await expect(self.page.get_by_text("Correct!")).to_be_visible()

    async def click_view_report(self):
        await self.page.locator("#view-report").click()

    async def verify_bug_found_first(self):
        await expect(self.page.get_by_role("heading", name="#1 Awesome! You found a bug.")).to_be_visible(timeout=30000)

    async def click_close_report(self):
        await self.page.get_by_role("button", name="Close").click()

    async def verify_more_bugs(self):
        await expect(self.page.get_by_text("There are more bugs in the find bugs page, please keep searching.")).to_be_visible(timeout=10000)

    async def click_close_more_bugs(self):
        await self.page.get_by_role("button", name="Close").click()

    async def click_item_dnk_yellow_shoes(self):
        await self.page.locator("#ec_product_image_effect_4481370").click()
        await self.page.wait_for_url("**/dnk-yellow-shoes/")
        return ProductPage(self.page)
    
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
