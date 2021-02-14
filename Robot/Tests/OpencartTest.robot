*** Settings ***
Library    SeleniumLibrary
Resource    ../PageObjects/OpencartPage.robot

Test Setup    Open Browser    ${URL}    ${BROWSER}
Test Teardown    Close Browser


*** Variables ***
${BROWSER}    chrome
${URL}    http://localhost


*** Test Cases ***
The page contains the title "Your Store"
    Go To   ${URL}
    ${TITLE}    Get Title
    Should Contain      ${TITLE}    Your Store

Clicking on the Tablets sidebar opens the Tablets page and has a product on it
    Go To    ${URL}/index.php?route=product/category&path=20
    Click Element    ${LIST_GROUP_ITEM}
    ${temp_elem}    Get Element Attribute    ${CAPTION_H4}    innerHTML
    Should Contain      ${temp_elem}    Samsung Galaxy Tab 10.1

Follow the link from the footer
    Go To    ${URL}
    Click Element    ${FOOTER}
    Location Should Be    http://localhost/about_us

Clicking on the banner opens another page
    Go To    ${URL}/index.php?route=product/category&path=20
    Click Element    ${BANNER}
    Location Should Be    http://localhost/index.php?route=product/manufacturer/info&manufacturer_id=7

Logout Admin
    Go To    ${URL}/admin/
    Login-Logout Admin
    Location Should Be    http://localhost/admin/index.php?route=common/login





