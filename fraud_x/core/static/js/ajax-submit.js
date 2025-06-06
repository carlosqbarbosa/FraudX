document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("fraud-form");
    const messageBox = document.getElementById("response-message");
    const messageText = document.getElementById("message-text");
    const closeButton = document.getElementById("close-message-btn");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log("✅ Response received:", data.message);
            messageText.innerText = data.message; 
            messageBox.classList.add("show");

            if (data.message) {
                messageText.innerText = data.message;
                messageBox.classList.add("show");

                if (!data.message.includes("Transaction No Fraud")) {
                    messageBox.classList.add("error");
                    closeButton.classList.add("error-button");
                } else {
                    messageBox.classList.remove("error");
                    closeButton.classList.remove("error-button");
                }
            }
        })
        .catch(error => console.error("❌ Error in request:", error));
    });

    closeButton.addEventListener("click", function () {
        console.log("🛠️ Closing message box.");
        messageBox.classList.remove("show");
    });
});