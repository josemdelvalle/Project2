const getCookie = (cookie_name) =>{
    // Construct a RegExp object as to include the variable name
    const re = new RegExp(`(?<=${cookie_name}=)[^;]*`);
    try{
      return document.cookie.match(re)[0];	// Will raise TypeError if cookie is not found
    }catch{
      return "this-cookie-doesn't-exist";
    }
  }
  
  firstName=getCookie("firstName");
  isLogedin=getCookie("Logedin");
  console.log(isLogedin);
  
//   if (isLogedin=="False");{
//     window.location.href = "/login.html";
//   }
// Test
//document.getElementById("container").innerHTML = "<p>This is a paragraph</p>"

// function createProductElement(srcImage, price, name){
//     newDiv = document.createElement("div");
//     document.getElementById("container").append(newDiv);
//     newDiv.innerHTML = "<image src=' " + srcImage + "'/> <p> name: " + 
//     name + "</p> <p>price: " + price;
//     // newDiv.id = "container" + id;
//     // document.getElementById("container" + id).innerHTML = 
// }

// Testing the ability to dynamically add product information into the website
// createProductElement("", 8, "ice cream");

// product1 = {
//     "srcImage": "",
//     "price": "91",
//     "name": "ice cream"
// };
// product2 = {
//     "srcImage": "",
//     "price": "53",
//     "name": "sundae"
// };
// product3 = {
//     "srcImage": "",
//     "price": "19",
//     "name": "cream"
// };

// allProducts = [];
// allProducts.push(product1);
// allProducts.push(product2);
// allProducts.push(product3);
// console.log(allProducts);

// for(i = 0; i < allProducts.length; i++){
//     console.log(i);
//     createProductElement(allProducts[i].srcImage, allProducts[i].price, allProducts[i].name);
// }


// let xttp = XMLHttpRequest();

// xttp.onReadyStateChange() = function(){
//     if (this.readyState == 4 && this.status == 200){
//         console.log(this.responseText);

//         let allProducts = JSON.parse(this.responseText);
//         for(let i = 0; i < allProducts.length; i++){
//             createProductElement(allProducts[i].srcImage, allProducts[i].price, allProducts[i].name);
//         }
//     }
// };

// url = "localhost:5000/products";
// xttp.open("GET", url, true);

// xttp.send();
