package servicetests;

import models.Order;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.mockito.internal.matchers.Or;
import org.testng.Assert;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;
import org.testng.annotations.TestInstance;
import repositories.OrderRepository;
import services.OrderService;

import java.util.ArrayList;
import java.util.List;

public class OrderServiceTester {

    @Mock
    OrderRepository orderRepo;

    @InjectMocks
    OrderService orderService;

    @BeforeSuite
    public void setUp() {
        orderRepo = new OrderRepository();
        orderService = new OrderService(orderRepo);

        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void getAllOrdersEmpty() {

        List emptyList = new ArrayList();
        Mockito.when(orderRepo.getAllOrders()).thenReturn(emptyList);
        List ordersList = orderService.getAllOrders();
        Assert.assertEquals(emptyList, ordersList);
    }

    @Test
    public void getAllOrdersNotEmpty() {

        List expectedList = new ArrayList();
        expectedList.add(new Order(1, 1, 1, 1, 1));
        expectedList.add(new Order(2, 1, 1, 1, 1));
        expectedList.add(new Order(3, 1, 1, 1, 1));
        expectedList.add(new Order(4, 1, 1, 1, 1));

        Mockito.when(orderRepo.getAllOrders()).thenReturn(expectedList);
        List ordersList = orderService.getAllOrders();
        Assert.assertEquals(expectedList, ordersList);
    }
}
