document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("toggle-btn");
    const contentWrapper = document.getElementById("content-wrapper");

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("closed"); // Toggle the sidebar collapse/expand
        contentWrapper.classList.toggle("expanded"); // Optional: use if you want to handle expanded content styling
    });
});
