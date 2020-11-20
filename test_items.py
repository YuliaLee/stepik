link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_add_to_basket_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, "The add to basket button wasn't found"

