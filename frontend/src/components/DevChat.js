import React from "react";
import Chat from "./Chat";
import "../style/DevChat.css";

function DevChat({ closeDevChat }) {
  return (
    <div className="chat">
      <button onClick={() => closeDevChat(false)}> X </button>
      <Chat />
    </div>
  );
}

export default DevChat;
