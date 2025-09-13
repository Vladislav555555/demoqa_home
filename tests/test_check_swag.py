from pages.swag_labs import SwagLabs

def test_icon_exists(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon() is True

def test_username_field_exists(browser):
        page = SwagLabs(browser)
        page.visit()
        assert page.exist_username_field() is True

def test_password_field_exists(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password_field() is True