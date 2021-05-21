let xttp = new XMLHttpRequest();

xttp.onreadystatechange = function() {
    console.log(this.readyState);
    if (this.readyState == 4 && this.status == 200){
        console.log(this.responseText);

        let allOrders = JSON.parse(this.responseText);
        let orderNumbers = [];
        for (let i = 0; i < allOrders.length; i++){
            console.log(allOrders[i].orderNumber);
            if (!orderNumbers.includes(i)){
                orderNumbers += i;
                console.log(i);
            }
        }

        console.log(orderNumbers);
        for(number in orderNumbers){
            // create view orders button
            document.getElementById("container").innerHTML += 
            `   <div>
                    <button id=${number}>Click Button</button>
                </div>
            `;
        }
    }
}

url = "http://localhost:7001/orders";
xttp.open("GET", url, true);

xttp.send();