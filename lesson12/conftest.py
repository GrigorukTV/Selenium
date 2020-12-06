import pytest
from classes.Browser import Browser
from classes.HomePage import HomePage
from classes.Catalog import Catalog
from classes.CatalogIdentifier import CatalogId
from classes.AccountLogin import  AccountLogin
from classes.AccountLoginAdm import AccountLoginAdm
from classes.Admin import Admin

def pytest_addoption(parser):
    parser.addoption("--browser",
                        action="store",
                        help="browser",
                        choices=['chrome','firefox'])
    parser.addoption("--url",
                        default="http://localhost/",
                        help="This is request url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")

@pytest.fixture()
def wd(browser, url):
    browser_page = Browser(browser, url)
    wd = browser_page.get_wd()
    yield wd
    browser_page.closeBrowser()

'''
фикстура для HomePage
'''
@pytest.fixture()
def home_page(wd):
    home = HomePage(wd)
    return home

'''
фикстура для Catalog
'''
@pytest.fixture()
def catalog(wd):
    catalog_products = Catalog(wd)
    return catalog_products

'''
фикстура для CatalogId
'''
@pytest.fixture()
def catalog_id(wd):
    catalog_product_id= CatalogId(wd)
    return catalog_product_id

'''
фикстура для AccountLogin
'''
@pytest.fixture()
def account_login(wd):
    user_account_login= AccountLogin(wd)
    return user_account_login

'''
фикстура для AccountLoginAdm
'''
@pytest.fixture()
def account_login_adm(wd):
    user_account_login_adm= AccountLoginAdm(wd)
    return user_account_login_adm

'''
фикстура для Admin
'''
@pytest.fixture()
def admin(wd):
    admin= Admin(wd)
    return admin