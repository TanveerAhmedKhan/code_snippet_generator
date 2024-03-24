
//Setting up event listener for enter
document.getElementById("messageInput").addEventListener("keypress", async (e) => {
    if (e.key == "Enter") {
        await sendMessage();
    }
});

async function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var message = messageInput.value.trim();
    
    if (message !== "") {
        appendMessage("You", message);

        let data_to_send = { query: message };
        messageInput.value = "";

        console.log(data_to_send);

        //Hit fastapi
        let resp = await fetch("http://localhost:8000/api/code_generator", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
            body: JSON.stringify(data_to_send)
        });

        resp = await resp.json();

        appendMessage("Code Generator", resp.code_snippet);
    }
}

function appendMessage(sender, message) {
    var chatBox = document.getElementById("chatBox");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.innerHTML = "<strong>" + sender + ":</strong> " + message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
