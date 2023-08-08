*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***

TestGmailLogin

    Open Browser     https://gmail.com/     chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Input Text    id:identifierId   yashreddy432@gmail.com
    Click Element       xpath://span[.='Next']
    Input Text    name:Passwd     yasodhabharath
    Sleep    2s
    Click Element   xpath://span[.='Next']
    Sleep    8s
    ${title}    Get Title
    Log To Console    ${title}

    IF    "${title}" == "Inbox (5) - yashreddy432@gmail.com - Gmail"
        Log To Console    Login Successful!!!!!!!!!!
    ELSE
        Log To Console    Gmail Login Fail......
    END

Open Google Sheet or Excel

    Click Element    xpath://a[@aria-label='Google apps']
    Select Frame    xpath://iframe[@name='app']
    Click Element    xpath://span[.='Sheets']
    Sleep    12s
    Switch Window    Google Sheets
    Click Element    xpath://img[@src='https://ssl.gstatic.com/docs/templates/thumbnails/sheets-blank-googlecolors.png']
    Sleep    5s

Enter Content
    Press Keys    //input[@id]    A1
    Input Text  //div[@class="cell-input"]     NAMES
    Sleep    2
    #To add content to the sheet
    Press Keys      //input[@id]    C1
    Press Key      //input[@id]     \\13
    Input Text    //div[@class="cell-input"]    EXPERIANCE
    Sleep    2s

Share with Mentor

    Click Element    xpath://div[@aria-label='Share. Private to only me. ']
    Input Text    xpath://input[contains(@class,'userInput')]     demo_test
    Click Element    xpath://button[.='Save']
    Select Frame    xpath://iframe[@class='share-client-content-iframe']
    Input Text    xpath://input[@type='text']      yasodhareddy432@gmail.com    ENTER
    Sleep    2s
    Click Element       xpath://span[@class=' VfPpkd-StrnGf-rymPhb-L8ivfd-fmcmS']    #ENTER

    Input Text    xpath://textarea[contains(@class,'VfPpkd')]       I am sharing a demo file
    Click Element    //button[.='Send']
    Sleep    4s



