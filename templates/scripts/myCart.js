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
      }else{

      }
    }
    xhr.send();
    
}
userId=getCookie("userId");
get_all_products_from_cart_by_user_id(userId)


function createProductElement(element){

}