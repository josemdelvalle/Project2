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
        ` <h1>All Placed Orders</h1>
        `
        for(number in orderNumbers){
            // create view orders button
            let id = parseInt(number) + 1;
            document.getElementById("container").innerHTML += 
            `   <div>
                    <button id=${id} onclick=openOrderView(${id})>Open order ${id}</button>
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
    for (i = 0; i < allOrderProducts.length; i++){
        if (productDict[allOrderProducts[i]]){
            productDict[allOrderProducts[i]] = productDict[allOrderProducts[i]] + 1;
        } else {
            productDict[allOrderProducts[i]] = 1;
        }
    }

    console.log(productDict);

    let top5 = [];
    for(var k in productDict){
        if (top5.length == 0){
            top5.push(productDict[k]);
        }
        
        for(i = 0; i < top5.length; i++){
            if (top5.includes(productDict[k])){
                break;
            }

            if(top5[i] >= productDict[k]){
            }
            
            if(top5[i] <= productDict[k]){
                top5.push(top5[i]);
                top5[i] = productDict[k];
            } else {
                if(top5.length < 6){
                    top5.push(productDict[k]);
                }
            }
        }
    }

    console.log(top5);

    function getKeyByValue(object, value) {
        for (var prop in object) {
            if (object.hasOwnProperty(prop)) {
                if (object[prop] === value)
                return prop;
            }
        }
    }

    let popular = [];
    for(i = 0; i < top5.length; i++){
        popular.push(getKeyByValue(productDict, top5[i]));
        console.log(top5[i]);
    }

    console.log(popular);

    let element = document.getElementById("popular");
    element.innerHTML += "<h1> Most popular products </h1>"
    for (i = 0; i < popular.length; i++){
        let xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200){
                let product = JSON.parse(this.responseText);
                element.innerHTML += 
                `   <div>
                        <p>${top5[0]} ${product.productName}</p>
                    </div>
                `;
                
                top5.splice(0, 1);
            }
        }

        let destination = "http://localhost:5000/products/" + popular[i];
        xhr.open("GET", destination, true);

        xhr.send();
    }
}