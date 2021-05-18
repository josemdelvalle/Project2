package models;

public class Order {

    private int orderId;
    private int orderNumber;
    private int quantity;
    private int product_id;
    private int user_id;

    public Order() {}

    public Order(int orderId, int orderNumber, int quantity, int product_id, int user_id) {
        super();
        this.orderId = orderId;
        this.orderNumber = orderNumber;
        this.quantity = quantity;
        this.product_id = product_id;
        this.user_id = user_id;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public int getProduct_id() {
        return product_id;
    }

    public void setProduct_id(int product_id) {
        this.product_id = product_id;
    }

    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
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
