*** Settings ***
Documentation    List all sub-breed images

Library    RequestsLibrary

Test Template    Passing Breed To Posts Handler

*** Variables ***
${DOG}    https://dog.ceo

*** Test Cases ***     breed     status
First Breed    afghan    200
Second Breed    basset    200

*** Keywords ***
Passing Breed To Posts Handler
    [Arguments]    ${breed}    ${status}
    Create Session    json_place    url=${DOG}    disable_warnings=1
    ${resp}    GET On Session    json_place    /api/breed/hound/${breed}/images    expected_status=${status}
    Should Be Equal As Integers    ${status}    ${resp.status_code}


