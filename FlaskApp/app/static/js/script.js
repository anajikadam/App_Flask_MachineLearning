document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("greetBtn");
    const message = document.getElementById("greetMsg");

    button.addEventListener("click", () => {
        message.textContent = "Hello, Flask Developer! 🎉";
    });
});
