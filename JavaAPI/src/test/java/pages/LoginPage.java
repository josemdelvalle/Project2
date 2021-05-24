package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
    @FindBy(id = "usernameInput")
    private WebElement username;

    @FindBy(id = "passwordInput")
    private WebElement password;

    @FindBy(id = "loginButton")
    private WebElement loginButton;

    @FindBy(xpath = "/html/body/div[2]/div[1]/p")
    private WebElement firstProduct;

    public LoginPage(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    public WebElement inputUsername() {
        return this.username;
    }

    public WebElement inputPassword() {
        return this.password;
    }

    public void clickLogin() {
        this.loginButton.click();
    }

    public WebElement getPopularProduct() {
        return this.firstProduct;
    }
}
