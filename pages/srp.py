from playwright.async_api import Page, expect

class SRPPage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self):
        await self.page.goto("https://academybugs.com/find-bugs")

    async def click_close_cookies(self):
        await self.page.get_by_text("Functional only").click()

    async def click_filter_10_items(self):
        await self.page.locator("a.what-we-offer-pagination-link:nth-child(2)").click()

    async def verify_bug_popup(self):
        await expect(self.page.get_by_text("What did you find out?")).to_be_visible(timeout=60000)

    async def check_item_crash(self):
        await self.page.locator('input[type="radio"][value="Crash"]').check()

    async def check_bug001_text(self):
        await self.page.locator('input[type="radio"][value="The selected number of results is displayed according to the clicked buttons"]').check()

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