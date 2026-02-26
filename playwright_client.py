from playwright.sync_api import sync_playwright, Playwright
from rich import print

def run(playwright):
    start_url = "https://www.sportsbet.com.au/betting/soccer"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    # Wait for the specific container or elements to load to avoid scraping an empty page
    page.wait_for_selector('div[data-automation-id$="-competition-event-card"]')

    # Locate all event cards. The $= means "ends with"
    # This targets elements like data-automation-id="10151698-competition-event-card"
    event_cards = page.locator('div[data-automation-id$="-competition-event-card"]')
    
    # Get the count to iterate over them safely
    count = event_cards.count()
    print(f"Found {count} events.")

    for i in range(count):
        card = event_cards.nth(i)
        # Find the <a> tag within this specific card to get the link
        link_element = card.locator('a')
        
        if link_element.count() > 0:
            href = link_element.get_attribute('href')
            print(f"Match Link: {href}")

    # browser.close() # Don't forget to close the browser eventually


with sync_playwright() as playwright:
    run(playwright)

#data-automation-id="1165208673-three-outcome-captioned-text"