class Displates:

    def __init__(self, link, size):

        self.link = link
        self.size = size

class size_choice:

    def size_options(self):
        if self.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]/img').click()
        if self.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]/img').click()
        if self.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]/img').click()

        addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
        addtocart += 1



