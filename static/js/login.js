document.addEventListener("DOMContentLoaded", function () {
    function updateGreeting() {
        let now = new Date();
        let hour = now.getHours();
        let greetingText = document.getElementById("greeting-text");

        if (hour >= 5 && hour < 12) {
            greetingText.innerHTML = "Good Morning!";
        } else if (hour >= 12 && hour < 18) {
            greetingText.innerHTML = "Good Afternoon!";
        } else {
            greetingText.innerHTML = "Good Evening!";
        }
    }

    updateGreeting();
});


document.addEventListener("DOMContentLoaded", function () {
    const togglePasswordButtons = document.querySelectorAll(".toggle-password");

    togglePasswordButtons.forEach(button => {
        button.addEventListener("click", function () {
            const input = this.previousElementSibling;
            const icon = this.querySelector("i");

            if (input.type === "password") {
                input.type = "text";
                icon.classList.remove("fa-eye-slash");
                icon.classList.add("fa-eye"); // Open eye when password is visible
            } else {
                input.type = "password";
                icon.classList.remove("fa-eye");
                icon.classList.add("fa-eye-slash"); // Closed eye when password is hidden
            }
        });
    });
});