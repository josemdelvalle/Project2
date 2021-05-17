package models;

public class Order {

    private int orderId;
    private int orderNumber;

    public Order() {}

    public Order(int orderId, int orderNumber) {
        super();
        this.orderId = orderId;
        this.orderNumber = orderNumber;
    }

    public int getOrderId() {
        return orderId;
    }

    public void setOrderId(int orderId) {
        this.orderId = orderId;
    }

    public int getOrderNumber() {
        return orderNumber;
    }

    public void setOrderNumber(int orderNumber) {
        this.orderNumber = orderNumber;
    }
}
