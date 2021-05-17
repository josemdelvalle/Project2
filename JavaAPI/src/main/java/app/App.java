package app;

import controllers.OrderController;
import io.javalin.Javalin;
import repositories.OrderRepository;
import services.OrderService;

public class App {
    public static void main(String[] args) {

        Javalin app = Javalin.create(config -> config.enableCorsForAllOrigins());
        establishRoutes(app);

        app.start(7001);
    }

    public static void establishRoutes(Javalin app) {
        OrderRepository orderRepository = new OrderRepository();
        OrderService orderService = new OrderService(orderRepository);
        OrderController orderController = new OrderController(orderService);

        app.get("/orders", orderController.getAllOrders);

    }
}
