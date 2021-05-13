const btn = document.getElementById('loginButton');
btn.addEventListener('click', (e) => {
    e.preventDefault(); // disable the refresh on the page when submit
    var xhr = new XMLHttpRequest();
    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;
    xhr.open("POST", "http://localhost:5000/login", true);
    // xhr.withCredentials = true;
    console.log(username)
    console.log(password)
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        userName: username,
        password: password
    }));

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 201 ||200) {
            console.log("HERE")
        }else{
            console.log("hello")
        }
    }
    
});