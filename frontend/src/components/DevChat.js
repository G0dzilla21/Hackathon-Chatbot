import React from "react";
import Chat from "./Chat";

function DevChat({ closeDevChat }) {
  return (
    <Chat closeChat={closeDevChat} />
  );
}

export default DevChat;
