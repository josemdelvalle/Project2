var user;
const btn = document.getElementById('loginButton');
btn.addEventListener('click', (e) => {
    e.preventDefault(); // disable the refresh on the page when submit
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;
    xhr.open("POST", "http://127.0.0.1:5000/login", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        userName: username,
        password: password
    }));

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText)
            user = JSON.parse(this.responseText);

            if (user.isAdmin == true) {
                document.cookie = `userId=${user.userId}; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/adminPage.html`;
                document.location.href = "adminPage.html";
            
            } else {
                document.cookie = `userId=${user.userId}; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/storePage.html`;
                document.cookie = `userId=${user.userId}; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/productOverview.html`;
                document.cookie = `userId=${user.userId}; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/adminPage.html`;
                document.location.href = "storePage.html";
            }


        } else {
            console.log(this.responseText);
        }
    }

});