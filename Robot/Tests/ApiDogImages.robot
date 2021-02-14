*** Settings ***
Documentation    Display several random images from an entire dog collection

Library    RequestsLibrary

Test Template    Passing Count To Posts Handler

*** Variables ***
${DOG}    https://dog.ceo

*** Test Cases ***    count     status
Two Images    2    200
Three Images    3    200

*** Keywords ***
Passing Count To Posts Handler
    [Arguments]    ${count}  ${status}
    Create Session    json_place    url=${DOG}    disable_warnings=1
    ${resp}    GET On Session    json_place    /api/breed/hound/afghan/images/random/${count}    expected_status=${status}
    ${size}     Get length     ${resp.json()['message']}
    Should Be Equal As Integers    ${size}    ${count}


