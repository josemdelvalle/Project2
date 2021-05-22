userId=getCookie("userId");
get_all_products_from_cart_by_user_id(userId);
const tableContent =document.getElementById("tableContent");
const priceTag=document.getElementById("totalPrice");
const submitOrderBtn = document.getElementById("submitOrderBtn");
var productArr;
function get_all_products_from_cart_by_user_id(user_id){
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true
    xhr.open("GET", `http://127.0.0.1:5000/cart/${user_id}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        productArr=JSON.parse(this.responseText);
        if (productArr){
          productArr.forEach(createProductElement);
          setTotalPrice(productArr);
        }
        
      
      }else{
        priceTag.innerHTML=0;
      }
    }
    xhr.send();
}

function createProductElement(element){
  tableContent.innerHTML+=
    `
      <tr>
      <td>${element.productName}</td>
      <td>${element.productPrice}</td>
      <td>${element.quantity}</td>
      <td><button name="${element.cartId}" class="cartBtn" onclick="delete_item_from_cart(this.name)">X</button></td>
     </tr>
    `;
}

function setTotalPrice(products){
  var  x=0;
  products.forEach(function(element) {
    x = x +element.quantity* element.productPrice;
  });
  priceTag.innerHTML=x;
}

function delete_item_from_cart(cartId){
  console.log(cartId);
  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true
  xhr.open("DELETE", `http://127.0.0.1:5000/cart/${cartId}`, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      tableContent.innerHTML="";
      get_all_products_from_cart_by_user_id(userId);
    }else{
      console.log(this.responseText);
    }
  }
  xhr.send();

}

function addOrder(){
  var xhr2 = new XMLHttpRequest();
  xhr2.withCredentials = true;
  xhr2.open("POST", "http://127.0.0.1:5000/order", true);
  xhr2.setRequestHeader('Content-Type', 'application/json');
  xhr2.send(JSON.stringify({
    userId:userId
  }));
  xhr2.onreadystatechange = function (){
   console.log("here");
  }
}