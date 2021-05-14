const btn = document.getElementById('loginButton');
btn.addEventListener('click', (e) => {
    e.preventDefault(); // disable the refresh on the page when submit
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true
    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;
    xhr.open("POST", "http://127.0.0.1:5000/login", true);
    ;
    console.log(username)
    console.log(password)
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        userName: username,
        password: password
    }));

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText)
            responseObject= JSON.parse(this.responseText);
            console.log(responseObject);

            document.cookie = "username=John Doe";
        //  window.location.href = "/storePage.html";
        document.cookie = "username=John Doe; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/storePage.html";
        


        }else{
            console.log(this.responseText);
        }
    }
    
});