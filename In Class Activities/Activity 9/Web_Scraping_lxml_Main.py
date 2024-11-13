import Web_Scraping_xml as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)
    uni_name_approach_1 = main_tree.xpath('/html/body/header/div/a/text()')
    print(uni_name_approach_1)

    uni_name_approach_2 = main_tree.xpath('/html/body/header/div/a/text()')
    print(uni_name_approach_2)
    # Let us see how many divs are they under this section
    all_divs = main_tree.xpath('//*[@id="wvu-main"]/div')
    # This will display the number of sections
    print(str(len(all_divs)))
    # Interact with the first div
    first_div = all_divs[0]
    # This will get the number of sections (divs) under the first div.
    print(str(len(first_div)))
    # This will extract the Goblins, ghouls and gourds statement from the website.
    goblins = main_tree.xpath('//*[@id="wvu-main"]/div[1]/div[1]/div/h1/span/text()')
    print(goblins)
    your_guide_approach_1 = main_tree.xpath('/html/body/main/div[3]/div/div[1]/h2/text()')
    print(your_guide_approach_1)

    your_guide_approach_2 = main_tree.xpath('// *[ @ id = "resources"] / div / div[1] / h2/text()')
    print(your_guide_approach_2)


if __name__ == "__main__":
    main()
