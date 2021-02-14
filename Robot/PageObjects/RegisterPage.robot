*** Settings ***
Library  SeleniumLibrary
Library  DatabaseLibrary


*** Variables ***
${First_Name}   css=#input-firstname
${Last_Name}    css=#input-lastname
${E-Mail}    css=#input-email
${Telephone}    css=#input-telephone
${Pass}    css=#input-password
${Pass_confirm}    css=#input-confirm
${Checkbox}     css=.pull-right input[name="agree"]
${Button}      css=.pull-right input[value="Continue"]


*** Keywords ***
Register Customer
    Input Text    ${First_Name}     Вася
    Input Text    ${Last_Name}      Пупкин
    Input Text    ${E-Mail}     test@mail.ru
    Input Text    ${Telephone}      +79100000000
    Input Text    ${Pass}   12345678
    Input Text    ${Pass_confirm}   12345678
    Select Checkbox    ${Checkbox}
    Click Button      ${Button}