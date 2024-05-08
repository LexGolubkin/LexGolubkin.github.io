let tg = window.Telegram.WebApp;

let name = "";
let email = "";
let phone = "";

let doing = document.getElementById("doing");
let order = document.getElementById("order");
let close = document.getElementById("close");

tg.expand();

doing.addEventListener("click", () => {
    document.getElementById("main").style.display = "none";
    document.getElementById("form").style.display = "block";
    document.getElementById("user_name").value = tg.initDataUnsafe.user.first_name + " "
                                                + tg.initDataUnsafe.user.last_name;
});

close.addEventListener("click", () => {
    name = document.getElementById("user_name").value;
    email = document.getElementById("user_email").value;
    phone = document.getElementById("user_phone").value;

    let data = {
        name: name,
        email: email,
        phone: phone
    };
    tg.sendData(JSON.stringify(data));

    tg.close();
});
