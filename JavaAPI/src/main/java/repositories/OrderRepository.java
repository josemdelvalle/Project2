package repositories;

import models.Order;
import util_orders.JDBCConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class OrderRepository {
    public static Connection conn = JDBCConnection.getConnection();

    public OrderRepository() {}

    public List<Order> getAllOrders() {
        try {
            String sql = "SELECT * FROM orders";
            PreparedStatement ps = conn.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            ArrayList orders = new ArrayList();

            while(rs.next()) {
                orders.add(this.buildOrder(rs));
            }

            return orders;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    public Order buildOrder(ResultSet rs) throws SQLException {
        Order d = new Order();
        d.setOrderId(rs.getInt("order_id"));
        d.setOrderNumber(rs.getInt("order_number"));
        return d;
    }
}
