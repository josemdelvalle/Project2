var getCookie = (cookie_name) =>{
    // Construct a RegExp object as to include the variable name
    const re = new RegExp(`(?<=${cookie_name}=)[^;]*`);
    try{
      return document.cookie.match(re)[0];	// Will raise TypeError if cookie is not found
    }catch{
      return "this-cookie-doesn't-exist";
    }
  }
  productId= getCookie("productId");
document.getElementById("productName").innerHTML =productId;


var product;
var xhr = new XMLHttpRequest();
xhr.withCredentials = true
xhr.open("GET", `http://127.0.0.1:5000/products/${productId}`, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText)
      product=JSON.parse(this.responseText);
      console.log(product);
      document.getElementById("productName").innerHTML =product.productName;
      document.getElementById("productDescription").innerHTML =product.description;
      document.getElementById("productPrice").innerHTML =product.productPrice;
      price=product.productPrice;
      document.getElementById("productImg").src = `/imgs/${product.productId}.jpg`;

    }else{
  
    }
}
xhr.send();

const productPrice=document.getElementById("productPrice");
const productQuantity=document.getElementById("productQuantity");

const changePrice=function (e){
  productPrice.innerHTML=e.target.value *product.productPrice;
  console.log(price)
};


productQuantity.addEventListener("input",changePrice);
productQuantity.addEventListener('propertychange', changePrice);

