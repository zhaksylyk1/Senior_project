document.getElementById("loginBtn").addEventListener("click", function() {
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("registerForm").style.display = "none";
});

document.getElementById("registerBtn").addEventListener("click", function() {
    document.getElementById("registerForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
});

document.getElementById("togglePassword").addEventListener("click", function() {
    const passwordInput = document.getElementById("passwordInput");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
});

function login() {
    // Implement login logic
}

function register() {
    // Implement registration logic
}
