package util_orders;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Properties;

public class JDBCConnection {

    private static Connection conn = null;

    public static Connection getConnection() {

        if (conn == null) {
            try {
                FileInputStream input = new FileInputStream(
                        JDBCConnection.class.getClassLoader().getResource("connection.properties").getFile()
                );
                Properties props = new Properties();
                props.load(input);

                String url = props.getProperty("url");
                String username = props.getProperty("username");
                String password = props.getProperty("password");

                conn = DriverManager.getConnection(url, username, password);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        return conn;
    }

    public static void main(String[] args) {
        Connection conn1 = getConnection();
        System.out.println(conn1);
    }
}

