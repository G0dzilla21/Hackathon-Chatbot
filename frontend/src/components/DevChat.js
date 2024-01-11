import React from "react";
import "../style/DevChat.css";
import Chat from "./Chat";

function DevChat({ closeDevChat }) {
  return (
    <div className="chat-container">
      <div className="chat-header">
        <button onClick={() => closeDevChat(false)}>X</button>
      </div>
      <Chat />
    </div>
  );
}

export default DevChat;
