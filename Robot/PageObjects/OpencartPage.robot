*** Settings ***
Library  SeleniumLibrary
Library  DatabaseLibrary


*** Variables ***
${FOOTER}   css=footer .col-sm-3:first-child li:first-child a
${BANNER}   css=#banner0
${LIST_GROUP_ITEM}    css=.list-group-item:nth-child(6)
${CAPTION_H4}   css=.caption h4 > a:first-child
${LOGIN}   css=#input-username
${PASS}   css=#input-password
${ENTER}    css=#input-password
${LOG_OUT}    css=.navbar-right > li:last-child a


*** Keywords ***
Login-Logout Admin
    Input Text    ${LOGIN}  user
    Input Text    ${PASS}   bitnami
    Press Keys    ${ENTER}    ENTER
    Click Element    ${LOG_OUT}