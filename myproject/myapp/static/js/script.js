// document.getElementById("loginBtn").addEventListener("click", function() {
//     document.getElementById("loginForm").style.display = "block";
//     document.getElementById("registerForm").style.display = "none";
// });

// document.getElementById("registerBtn").addEventListener("click", function() {
//     document.getElementById("registerForm").style.display = "block";
//     document.getElementById("loginForm").style.display = "none";
// });

// document.getElementById("togglePassword").addEventListener("click", function() {
//     const passwordInput = document.getElementById("passwordInput");
//     if (passwordInput.type === "password") {
//         passwordInput.type = "text";
//     } else {
//         passwordInput.type = "password";
//     }
// });

// function login() {
//     // Implement login logic
// }

// function register() {
//     // Implement registration logic
// }

const parallax = document.querySelector('.parallax');
const front = document.querySelector('.front-layer');
const back = document.querySelector('.back-layer');

const sFront = 150;
const sBack = 400;
parallax.addEventListener("mousemove", e => {
    const x = e.clientX;
    const y = e.clientY;

    front.style.transform = `translateX(${x/sFront}%) translateY(${y/sFront}%)`;
    back.style.transform = `translateX(${x/sBack}%) translateY(${y/sBack}%)`;

    // front.style.

    // front.style.transform = "translate(" + (x / sFront) + "%, " + (y / sFront) + "%)";
    // back.style.transform = "translate(" + (x / sBack) + "%, " + (y / sBack) + "%)";
    
    // front.style.transform = "translate(${x / sFont}%, ${y / sFont}% )";
    // back.style.transform = "translate(${x / sBack}%, ${y / sBack}% )";
});
