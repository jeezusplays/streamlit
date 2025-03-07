import streamlit as st
import streamlit.components.v1 as components

html_code = """
<html>
  <head>
    <script>
      // Disable copy event
      document.addEventListener('copy', function(e) {
        e.preventDefault();
      });
      
      // Disable paste event
      document.addEventListener('paste', function(e) {
        e.preventDefault();
      });

      // Disable right click (context menu)
      document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
      });
    </script>
    <style>
      /* Disable text selection */
      body {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        font-family: sans-serif;
      }

        #chat-container {
        max-height: 500px;
        overflow-y: auto;
      }
    </style>
  </head>
  <body>
    <div class="chat-container">
        <h1>💬 Chatbot</h1>
        <p>🚀 A simple chatbot interface</p>
        <div id="chatBox" class="chat-box"></div>
        <input type="text" id="userInput" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>
    </div>
  </body>

  <script>
        function sendMessage() {
            let inputField = document.getElementById("userInput");
            let message = inputField.value.trim();
            if (message === "") return;
            
            let chatBox = document.getElementById("chatBox");
            let userMessage = document.createElement("p");
            userMessage.classList.add("user-message");
            userMessage.textContent = "You: " + message;
            chatBox.appendChild(userMessage);
            inputField.value = "";

            setTimeout(() => {
                let botMessage = document.createElement("p");
                botMessage.classList.add("bot-message");
                botMessage.textContent = "Bot: " + "How can I help you?";
                chatBox.appendChild(botMessage);
                chatBox.scrollTop = chatBox.scrollHeight;
            }, 1000);
        }
    </script>
</html>
"""

components.html(html_code, height=300)