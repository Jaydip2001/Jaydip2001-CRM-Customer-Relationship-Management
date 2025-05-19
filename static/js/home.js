document.addEventListener("DOMContentLoaded", function () {
    console.log("CRM Home Page Loaded!");

    // Minimalist Button Hover Effects
    document.querySelectorAll(".animate-btn").forEach(button => {
        button.addEventListener("mouseenter", () => {
            button.style.transform = "translateY(-2px)";
        });

        button.addEventListener("mouseleave", () => {
            button.style.transform = "translateY(0px)";
        });
    });

});



