*** Settings ***
Library    RequestsLibrary
Library     JSONLibrary

*** Variables ***
${DOG}    https://dog.ceo
${message}    blood
${respons}    success

*** Test Cases ***
Test Dog Status Code
    [Documentation]    Checking the request status of the page with a picture
    Create Session    json_place    ${DOG}
    ${resp}    GET On Session    json_place    /api/breed/hound/afghan/images
    Should Be Equal As Integers    200    ${resp.status_code}

Test Dog Messege
    [Documentation]    Checking for the existence of a value
    Create Session    json_place    ${DOG}
    ${resp}    GET On Session    json_place    /api/breed/hound/list
    Should Be Equal     ${message}    ${resp.json()['message'][2]}

Test Dog Status Response
    [Documentation]    Checking the status in the response
    Create Session    json_place    ${DOG}
    ${resp}    Get On Session    json_place    /api/breeds/image/random
    Should Be Equal     ${respons}    ${resp.json()['status']}


