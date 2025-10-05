var password = prompt("Apa Password Kamu ?");

if (password == "Momentum") {
    document.write("<p>Password yang anda masukan benar yaitu : " + password + "</p>");
} else {
    alert("Maaf password anda salah .. silakan coba lagi ");
    window.location = "password.html";
}