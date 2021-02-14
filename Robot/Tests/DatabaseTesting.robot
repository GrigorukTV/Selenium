*** Settings ***
Library  String
Library    SeleniumLibrary

Resource    ../PageObjects/RegisterPage.robot
Resource    ../Resources/DataBase.robot


Suite Setup     Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
Suite Teardown      Disconnect From Database

Test Setup    Open Browser    ${URL}    ${BROWSER}
Test Teardown    Close Browser


*** Variables ***
${BROWSER}    chrome
${URL}    http://localhost
${DBName}    bitnami_opencart
${DBUser}    bn_opencart
${DBPass}
${DBHost}    0.0.0.0
${DBPort}    3307
${TEST_EMAIL}    test@mail.ru


*** Test Cases ***
Add account using Db validation

    [Documentation]    Register a new user using the user interface and check if it is up to date in the database
    [Tags]    DB    AddAccount
    [Teardown]    Run Keywords    Execute Sql String  delete from ${CUSTOMER_DB} where email = '${TEST_EMAIL}'
    ...  AND  Close Browser
    Go To    ${URL}/index.php?route=account/register
    Register Customer
    Wait Until Keyword Succeeds    3 sec  1 sec  Check customer In Database    ${TEST_EMAIL}







