function createProductElement(element){
    document.getElementById("productRow").innerHTML+=
    `    <div class="col-4 productCard">
                <button onclick=goToProductOverview(this.name) name="${element.productId}">
                    <img class="productImg"
                    src="/imgs/${element.productId}.jpg">
                    <div>${element.productName}</div>
                    <div>$${element.productPrice}</div>
                </button>
            </div>
    `;
}
function goToProductOverview(productId){
  document.cookie = `productId=${productId}; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/productOverview.html`;
  document.location.href = "productOverview.html";
}

// allProducts = [];
// allProducts.push(product1);
// allProducts.push(product2);
// allProducts.push(product3);
// console.log(allProducts);
// for(i = 0; i < allProducts.length; i++){
//     console.log(i);
//     createProductElement(allProducts[i].srcImage, allProducts[i].price, allProducts[i].name);
// }



var xhr = new XMLHttpRequest();
xhr.withCredentials = true
xhr.open("GET", "http://127.0.0.1:5000/products", true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText)
      productArr=JSON.parse(this.responseText);
      productArr.forEach(createProductElement);
    


    }else{
  
    }
}
xhr.send();