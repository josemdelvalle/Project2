let xttp = new XMLHttpRequest();

xttp.onreadystatechange = function() {
    console.log(this.readyState);
    console.log(this.responseText);
}

url = "https://127.0.0.0:5000/orders";
xttp.open("GET", url, true);

xttp.send();