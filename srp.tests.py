import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import expect

async def run(playwright):
    browser = await playwright.firefox.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://academybugs.com/find-bugs") 

    # Wait for the popup to appear and then click the button
    await page.get_by_text("Functional only").click()

    #Bug #1: Number of items displayed
    await page.locator("a.what-we-offer-pagination-link:nth-child(2)").click()
    await expect(page.get_by_text("What did you find out?")).to_be_visible(timeout=60000)
    await page.locator('input[type="radio"][value="Crash"]').check()
    await page.locator('input[type="radio"][value="The selected number of results is displayed according to the clicked buttons"]').check()
    await page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Correct!")).to_be_visible()
    await page.locator("#view-report").click()

    await expect(page.get_by_role("heading", name="#1 Awesome! You found a bug.")).to_be_visible(timeout=30000)
    await page.get_by_role("button", name="Close").click()

    await expect(page.get_by_text("There are more bugs in the find bugs page, please keep searching.")).to_be_visible(timeout=10000)
    await page.get_by_role("button", name="Close").click()

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())