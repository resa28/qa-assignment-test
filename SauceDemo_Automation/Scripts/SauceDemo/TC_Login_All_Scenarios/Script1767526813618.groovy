import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import org.openqa.selenium.Keys

WebUI.openBrowser('')
WebUI.navigateToUrl('https://www.saucedemo.com/')

// Clear fields
WebUI.clearText(findTestObject('SauceDemo/Login/input_username'))
WebUI.clearText(findTestObject('SauceDemo/Login/input_password'))

// Input username
if (username != null && username.trim() != '') {
    WebUI.setText(findTestObject('SauceDemo/Login/input_username'), username)
}

// Input password
if (password != null && password.trim() != '') {
    WebUI.setText(findTestObject('SauceDemo/Login/input_password'), password)
}

// ENTER key scenario
if (expected == 'ENTER') {
    WebUI.sendKeys(findTestObject('SauceDemo/Login/input_password'), Keys.chord(Keys.ENTER))
} else {
    WebUI.click(findTestObject('SauceDemo/Login/button_login'))
}

// Validation
switch (expected) {

    case 'SUCCESS':
    case 'ENTER':
        WebUI.verifyElementPresent(findTestObject('SauceDemo/Login/label_products'), 5)
        break

    case 'DASHBOARD':
        WebUI.verifyMatch(WebUI.getUrl(), '.*inventory.html.*', true)
        break

    case 'PRODUCT':
        WebUI.verifyElementPresent(findTestObject('SauceDemo/Login/product_list'), 5)
        break

    case 'MENU':
        WebUI.verifyElementPresent(findTestObject('SauceDemo/Login/button_menu'), 5)
        break

    case 'NO_REDIRECT':
        WebUI.verifyElementNotPresent(findTestObject('SauceDemo/Login/label_products'), 3)
        break

    default:
        WebUI.verifyElementPresent(findTestObject('SauceDemo/Login/label_error'), 5)
        break
}

WebUI.closeBrowser()
