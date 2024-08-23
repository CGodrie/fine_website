$(document).ready(function () {
  const chatContainer = $("#chat-container");

  if (chatContainer.length) {
    const messageList = $("#message-list");
    const user = chatContainer.attr("request-user");
    const discussionID = chatContainer.attr("discussion-id");
    const textAreaInput = $("#message-input");
    const sendButton = $("#send-button");
    let userScrolled = false;

    function sendMessage() {
      const messageContent = textAreaInput.val();

      $.ajax({
        type: "POST",
        url: `/chat/${discussionID}/send-message/`,
        data: {
          message_content: messageContent,
        },
        success: function () {
          console.log("Message sent successfully");

          textAreaInput.val("");
          sendButton.prop("disabled", true);

          // Si l'utilisateur n'a pas fait défiler manuellement ou est revenu tout en bas, faites défiler vers le bas
          if (!userScrolled || messageList.scrollTop() + messageList.innerHeight() === messageList.prop("scrollHeight")) {
            messageList.scrollTop(messageList.prop("scrollHeight"));
          }
        },
        error: function (error) {
          console.error("Error sending message", error);
        },
      });
    }

    textAreaInput.on("input", function () {
      const messageContent = textAreaInput.val();
      sendButton.prop("disabled", messageContent === "");
    });

    textAreaInput.on("keyup", function (event) {
      if (event.code === "Enter") {
        sendMessage();
      }
    });

    messageList.on("scroll", function () {
      userScrolled = messageList.scrollTop() + messageList.innerHeight() < messageList.prop("scrollHeight");
    });

    function updateChatUI(messages) {
      const isUserScrolledToBottom = messageList.scrollTop() + messageList.innerHeight() === messageList.prop("scrollHeight");

      messageList.empty();

      for (const message of messages) {
        const messageElement = $("<div></div>").addClass(
          `message-container ${
            message.user === user ? "user-active text-right" : "user-inactive text-left"
          }`
        );

        const bubbleClass = message.user === user ? "user-active-bubble" : "user-inactive-bubble";
        const userInfo = message.user !== user ? `<div class="user-info"><strong>${message.user}</strong></div>` : "";

        messageElement.html(
          `<div class="message-bubble ${bubbleClass}" style="word-wrap: break-word;">${userInfo}<span>${message.message}</span></div><span class="message-timestamp">${message.sent_at}</span>`
        );

        messageList.append(messageElement);
      }

      // Si l'utilisateur était en bas avant la mise à jour, faites défiler vers le bas
      if (!userScrolled || isUserScrolledToBottom) {
        messageList.scrollTop(messageList.prop("scrollHeight"));
      }
    }

    function fetchMessages() {
      $.ajax({
        type: "GET",
        url: `/chat/${discussionID}/get-messages/`,
        dataType: "json",
        success: function (data) {
          if (data.status === "success") {
            updateChatUI(data.messages);
          } else {
            console.error("Error fetching messages:", data.error_message);
          }
        },
        error: function (error) {
          console.error("Error fetching messages:", error);
        },
      });
    }

    fetchMessages();
    setInterval(fetchMessages, 1000);
  }
});
