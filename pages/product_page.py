from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT
        ).text

    def get_basket_total(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_be_success_message_with_product_name(self):
        product_name = self.get_product_name()
        success_message = self.get_success_message_product_name()
        assert product_name == success_message, (
            f"Expected product '{product_name}', but got '{success_message}'"
        )

    def should_be_success_message_with_price(self):
        product_price = self.get_product_price()
        basket_total = self.get_basket_total()
        assert product_price == basket_total, (
            f"Expected price '{product_price}', but got '{basket_total}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT
        ), "Success message is displayed, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT), (
            "Success message did not disappear as expected"
        )
