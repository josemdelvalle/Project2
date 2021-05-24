package behaviortests;

import cucumber.api.CucumberOptions;
import cucumber.api.testng.AbstractTestNGCucumberTests;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import pages.LoginPage;

import java.io.File;

@CucumberOptions(
        features = {"src/test/resources/admin_login.feature"},
        glue = {"steps"}
)

public class TestNGRunner extends AbstractTestNGCucumberTests {

    public static WebDriver driver;
    public static LoginPage loginPage;

    public TestNGRunner() {
    }

    @BeforeSuite
    public void setUp() {
        File file = new File("C:/Users/JMDel/Documents/Revature/Selenium/chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());

        driver = new ChromeDriver();
        loginPage = new LoginPage(driver);
    }

    @AfterSuite
    public void tearDown() {
        driver.quit();
    }
}
