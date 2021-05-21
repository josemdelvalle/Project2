function get_all_products_from_cart_by_user_id(user_id){
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true
    xhr.open("GET", `http://127.0.0.1:5000/cart/${user_id}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        productArr=JSON.parse(this.responseText);
         productArr.forEach(createProductElement);
         setTotalPrice(productArr);
         
      }else{

      }
    }
    xhr.send();
    
}
userId=getCookie("userId");
get_all_products_from_cart_by_user_id(userId)


function createProductElement(element){
  document.getElementById("tableContent").innerHTML+=
    ` 
     <tr>
      <td>${element.productName}</td>
      <td>${element.productPrice}</td>
      <td>${element.quantity}</td>
      <td></td>
     </tr>
    `;

}

const priceTag=document.getElementById("totalPrice");
function setTotalPrice(products){
  var  x=0;
  products.forEach(function(element) {
    x = x +element.quantity* element.productPrice;
    priceTag.innerHTML=x;
  });
 
}