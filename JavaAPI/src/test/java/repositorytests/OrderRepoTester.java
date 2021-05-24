package repositorytests;

import org.testng.Assert;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;
import repositories.OrderRepository;

import java.util.ArrayList;
import java.util.List;

public class OrderRepoTester {

    @BeforeSuite
    public static void setUp() {
        System.out.println("Starting all tests:");
    }

    @AfterSuite
    public static void breakDown() {
        System.out.println("All tests completed");
    }

    @Test
    public void getAllOrders() {
        OrderRepository orderRepo = new OrderRepository();
        List orderList = orderRepo.getAllOrders();
        Assert.assertFalse(orderList.isEmpty());
    }
}
