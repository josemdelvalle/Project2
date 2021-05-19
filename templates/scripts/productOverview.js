// Setting vars
const productPrice = document.getElementById("productPrice");
const productQuantity = document.getElementById("productQuantity");
var product;
productId = getCookie("productId");
userId = getCookie("userId");





// define changePrice function 
// and adding the listeners so that price will change on input change
const changePrice = function (e) {
  productPrice.innerHTML = e.target.value * product.productPrice;

};
productQuantity.addEventListener("input", changePrice);
productQuantity.addEventListener('propertychange', changePrice);




//getting the product from the database
//assigning the product variable
var xhr = new XMLHttpRequest();
xhr.withCredentials = true
xhr.open("GET", `http://127.0.0.1:5000/products/${productId}`, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    console.log(this.responseText)
    product = JSON.parse(this.responseText);
    console.log(product);
    document.getElementById("productName").innerHTML = product.productName;
    document.getElementById("productDescription").innerHTML = product.description;
    document.getElementById("productPrice").innerHTML = product.productPrice;
    document.getElementById("productImg").src = `/imgs/${product.productId}.jpg`;

  } else {

  }
}
xhr.send();




//Adding the product to the cart
function addToCart() {
  const qty = document.getElementById("productQuantity").value;
  var xhr2 = new XMLHttpRequest();
  xhr2.withCredentials = true;
  xhr2.open("POST", "http://127.0.0.1:5000/cart", true);
  xhr2.setRequestHeader('Content-Type', 'application/json');
  xhr2.send(JSON.stringify({
    productId: product.productId,
    userId: userId,
    quantity: qty
  }));
  xhr2.onreadystatechange = function () {
    console.log(this.responseText)
  }
}