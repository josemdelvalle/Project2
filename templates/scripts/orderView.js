var url = document.location.href,
        params = url.split('?')[1].split('&'),
        data = {}, tmp;

for (var i = 0, l = params.length; i < l; i++) {
    tmp = params[i].split('=');
    data[tmp[0]] = tmp[1];
}

console.log(data.id);

// Send AJAX call to retrieve information on start up for order
let xttp = new XMLHttpRequest();

var allOrders = [];
xttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200){
        let retrievedOrders = JSON.parse(this.responseText);
        
        
        for (i = 0; i < retrievedOrders.length; i++){
            // console.log(retrievedOrders[i].orderNumber);
            if (retrievedOrders[i].orderNumber == data.id){
                allOrders.push(retrievedOrders[i]);
            }
        }

        for (i = 0; i < allOrders.length; i++){
            // This is where product name will be displayed
            // Sends a request to the databse in order to retrieve
            // all product information
            let xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200){
                    // displays the name of the product retrieved
                    let object = JSON.parse(this.responseText);
                    console.log(object);
                    document.getElementById("container").innerHTML += 
                    `   <div>
                            <p>${object.productName}</p>
                        </div>
                    `;
                }
            }
        
            let location = "http://localhost:5000/products/" + allOrders[i].product_id;
            xhr.open("GET", location, true);
        
            xhr.send();
           
        }
    }
}

let request = "http://localhost:7001/orders";
xttp.open("GET", request, true);

xttp.send();
