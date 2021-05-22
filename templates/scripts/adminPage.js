let xttp = new XMLHttpRequest();

var allOrders;
xttp.onreadystatechange = function() {
    console.log(this.readyState);
    if (this.readyState == 4 && this.status == 200){
        // console.log(this.responseText);

        allOrders = JSON.parse(this.responseText);
        let orderNumbers = [];
        for (let i = 0; i < allOrders.length; i++){
            if (!orderNumbers.includes(allOrders[i].orderNumber)){
                orderNumbers.push(allOrders[i].orderNumber);
            }
        }

        // console.log(orderNumbers);
        document.getElementById("container").innerHTML += 
        ` <p>All Placed Orders</p>
        `
        for(number in orderNumbers){
            // create view orders button
            document.getElementById("container").innerHTML += 
            `   <div>
                    <button id=${number} onclick=openOrderView(${number})>Open order ${number}</button>
                </div>
            `;
        }

        mostPopularItems();
    }
}

url = "http://localhost:7001/orders";
xttp.open("GET", url, true);

xttp.send();

function openOrderView(id){
    document.location.href = "orderView.html?id=" + id;
}

function mostPopularItems(){
    let allOrderProducts = [];
    for (i = 0; i < allOrders.length; i++){
        allOrderProducts.push(allOrders[i].product_id);
    }

    console.log(allOrderProducts);

    let productDict = {};
    for (i = 0; i < allOrderProducts[i]; i++){
        if (productDict.includes(allOrderProducts[i])){
            
        }
    }
}