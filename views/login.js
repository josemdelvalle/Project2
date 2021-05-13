var xhr = new XMLHttpRequest();
const btn = document.getElementById('loginButton');
btn.addEventListener('click', (e) => {
    e.preventDefault(); // disable the refresh on the page when submit
    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;
    xhr.open("POST", "http://localhost:5000/login", true);
    // xhr.withCredentials = true;
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        userName: username,
        password: password
    }));
    xhr.onload = function () {
        if (this.readyState == 4 && (this.status == 200 || 204)) {
            var data = JSON.parse(this.responseText);
            console.log("Here");
        }


    }
});