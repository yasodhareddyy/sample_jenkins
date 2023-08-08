*** Settings ***
Library     SeleniumLibrary
Library     DateTime


*** Variables ***
${demo_url}     https://www.techlistic.com/p/selenium-practice-form.html
${browser}      chrome
*** Test Cases ***
Open demo file
    Open Browser    ${demo_url}     ${browser}
    Maximize Browser Window
    Sleep    2s

Fill Details
    Input Text    name:firstname    Surapareddy
    Input Text    name:lastname     Yasodha
    Select Radio Button        sex      Female
    Select Radio Button        exp      1
    ${date}     Get Current Date
    #Log To Console    ${date}
    Input Text    id:datepicker     ${date.split()[0]}
    Execute Javascript    window.scrollTo(0,document.body.scrollHeight)     #end page
    Click Element       id:profession-1
    Click Element       id:tool-2
    Select From List By Label   continents  South America
    Click Element   xpath://option[.='Wait Commands']
    Sleep    2

Choose file
    Choose File    xpath://input[@name='photo']    C:/Users/YasodhaS-3242/Desktop/all folders/power1.png
    Sleep    5
Downlod file
    Click Link    xpath://a[.='Click here to Download File']
    Sleep    2
    Close Browser