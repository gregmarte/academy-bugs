from playwright.async_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    async def click_no_items_button(self):
        await self.page.locator(".ec_cart_empty_button").click()

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