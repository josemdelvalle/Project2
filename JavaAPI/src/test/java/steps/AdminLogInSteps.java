package steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import pages.LoginPage;
import behaviortests.TestNGRunner;

public class AdminLogInSteps {
    public static WebDriver driver;
    public static LoginPage loginPage;


    @Given("^The User is on the login page$")
    public void the_User_is_on_the_login_page() {
        try {
            driver.get("http://127.0.0.1:5500/login.html");
            driver.manage().window().maximize();
            Thread.sleep(8000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @When("^The User inputs their username and password$")
    public void the_User_inputs_their_username_and_password() {
        try {
            loginPage.inputUsername().sendKeys("marc");
            loginPage.inputPassword().sendKeys("12345");
            Thread.sleep(8000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    @When("^The User clicks on the login button$")
    public void the_User_clicks_on_the_login_button() {
        try {
            loginPage.clickLogin();
            Thread.sleep(8000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    @Then("^The User is on the Administrator page$")
    public void the_User_is_on_the_Administrator_page() {
        try {
            Assert.assertEquals(driver.getTitle(), "Admin Page");
            Thread.sleep(8000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    @Then("^The User can see the most popular product to order$")
    public void the_User_can_see_the_most_popular_product_to_order() {
        try {
            Assert.assertNotEquals(loginPage.getPopularProduct().getText(), "");
            Thread.sleep(8000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
    static {
        driver = TestNGRunner.driver;
        loginPage = TestNGRunner.loginPage;
    }
}
