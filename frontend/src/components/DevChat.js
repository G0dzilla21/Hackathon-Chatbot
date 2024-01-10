import React from "react";
import Chat from "./Chat";

function DevChat({ closeDevChat }) {
  return (
    <div>
      <button onClick={() => closeDevChat(false)}> X </button>
      <Chat />
    </div>
  );
}

export default DevChat;
