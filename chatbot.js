let step = 0;
const userData = {};

function sendMessage() {
    const userInput = document.getElementById("userInput").value.trim();
    if (userInput === "") return; // Don't send empty messages

    displayMessage(userInput, "user-message");

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, "bot-message");
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById("userInput").value = ""; // Clear the input field
}

function displayMessage(message, className) {
    const chatbox = document.getElementById("chatbox");
    const messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.innerHTML = message; // Using innerHTML to allow for line breaks
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
}
