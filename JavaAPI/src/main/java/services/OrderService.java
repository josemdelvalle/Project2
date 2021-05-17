package services;

import models.Order;
import repositories.OrderRepository;

import java.util.List;

public class OrderService {

    private OrderRepository orderRepo;

    public OrderService(OrderRepository orderRepo) { this.orderRepo = orderRepo; }

    public List<Order> getAllOrders() {
        return orderRepo.getAllOrders();
    }
}

