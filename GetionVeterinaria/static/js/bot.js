const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const suggestionsList = document.getElementById("suggestions");

function showSuggestions() {
    const userMessage = userInput.value.toLowerCase();
    const partialMatches = Object.keys(chatbot_data).filter(key => key.toLowerCase().includes(userMessage));

    suggestionsList.innerHTML = "";

    if (partialMatches.length > 0) {
        partialMatches.forEach(match => {
            const listItem = document.createElement("li");
            listItem.textContent = match;
            listItem.onclick = () => {
                userInput.value = match;
                suggestionsList.innerHTML = ""; // Limpiar las sugerencias cuando se selecciona una
            };
            suggestionsList.appendChild(listItem);

            // Si la sugerencia coincide exactamente con una pregunta específica, muestra la respuesta
            if (match.toLowerCase() === userMessage) {
                const botResponse = chatbot_data[match];
                displayBotResponse(botResponse);
            }
        });
    } else {
        suggestionsList.innerHTML = ""; // Limpiar las sugerencias si no hay coincidencias parciales
    }
}

function displayBotResponse(response) {
    const chatBox = document.getElementById("chat-box");
    const botResponseDiv = document.createElement("div");
    botResponseDiv.textContent = `Bot: ${response}`;
    chatBox.appendChild(botResponseDiv);
}
