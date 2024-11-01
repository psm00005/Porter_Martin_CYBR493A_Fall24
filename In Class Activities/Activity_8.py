import Web_Scraping_xml as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    # To clear out the whitespace I went to, "https://www.ibm.com/docs/en/i/7.3?topic=functions-fnnormalize-space-function", for the normalize-space function.
    main_tree = wb.get_web_tree("https://www.wvu.edu")
# Getting the header for Mikayla's video.
    mikayala_video_header = main_tree.xpath('normalize-space(/html/body/main/div[1]/div[1]/div/p[3]/a[1]/text())')
    print('1.)', mikayala_video_header)
# Scraping the header from the scholarship info button.
    scholarship_info_header = main_tree.xpath('normalize-space(/html/body/main/div[2]/div/div/div/div/div[4]/a/span[2]/text())')
    print('2.)', scholarship_info_header)
# Grabbing the news header from the bottom of the page.
    news_header = main_tree.xpath('normalize-space(/html/body/main/div[6]/div/div[2]/div/div/h3/text())')
    print('3.)', news_header)
# Finding the events header also located at the bottom of the page.
    events_header = main_tree.xpath('normalize-space(/html/body/main/div[6]/div/div[1]/div[1]/h3/text())')
    print('4.)', events_header)
# Taking the header from the Mountaineers at Work section.
    mountaineers_header = main_tree.xpath('normalize-space(/html/body/main/div[5]/div/div[1]/div[2]/h2/text())')
    print('5.)', mountaineers_header)


if __name__ == "__main__":
    main()
