import Web_Scraping_beautiful_soup as ws


# Main function to initialize and run the scraper
def main():
    # Initialize the scraper with the base URL
    scraper = ws.WVUScraper("https://www.wvu.edu")

    # Scrape the main page and follow links
    data = scraper.follow_links(scraper.base_url, max_pages=3, delay=1)

    # # Print data for each page
    # for page in data:
    #     print("Page URL:", page['url'])
    #     print("Headings:", page['headings'])
    #     print("Links:", page['links'])

    # Example of grabbing a specific item using a CSS selector
    html = scraper.get_html(scraper.base_url)
    soup = scraper.parse_html(html)

    # Attempt to retrieve the main heading using an alternative selector
    main_heading = scraper.grab_specific_item(soup, ".wvu-masthead")
    print("Main Heading:", main_heading)

    main_heading = scraper.grab_specific_item(soup, ".wvu-nav-wrapper")
    for something in main_heading:
        print( something,'\t')

    # Attempt to retrieve paragraphs within the about section using an alternative selector
    about_paragraphs = scraper.grab_specific_item(soup, ".about-content p")
    print("About Section Paragraphs:")
    for para in about_paragraphs:
        print(para)


if __name__ == "__main__":
    main()
