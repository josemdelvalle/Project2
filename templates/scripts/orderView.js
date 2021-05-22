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

xttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200){
        let retrievedOrders = JSON.parse(this.responseText);
        let allOrders = [];
        
        for (i = 0; i < retrievedOrders.length; i++){
            // console.log(retrievedOrders[i].orderNumber);
            if (retrievedOrders[i].orderNumber == data.id){
                allOrders.push(retrievedOrders[i]);
            }
        }

        for (i = 0; i < allOrders.length; i++){
            // This is where all of the information of choice will
            // be displayed
            document.getElementById("container").innerHTML += 
            `   <div>
                    <p>${allOrders[i].product_id}</p>
                </div>
            `;
        }
    }
}

let request = "http://localhost:7001/orders";
xttp.open("GET", request, true);

xttp.send();