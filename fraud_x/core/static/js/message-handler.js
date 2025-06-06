document.addEventListener("DOMContentLoaded", function () {
    const messageBox = document.getElementById("response-message");
    const closeButton = document.getElementById("close-message-btn");

    if (messageBox && closeButton) {
        closeButton.addEventListener("click", function () {
            messageBox.style.display = "none";
        });
    }
});