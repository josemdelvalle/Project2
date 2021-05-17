package controllers;

import com.google.gson.Gson;
import io.javalin.http.Handler;
import models.Order;
import services.OrderService;

import java.util.List;

public class OrderController {

    private OrderService orderService;
    private Gson gson = new Gson();

    public OrderController(OrderService orderService) { this.orderService = orderService; }

    public Handler getAllOrders = (context) -> {

        List<Order> orders = this.orderService.getAllOrders();
        String ordersJSON = gson.toJson(orders);
        context.result(ordersJSON);
    };
}

