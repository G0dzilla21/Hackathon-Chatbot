import React, { useState } from "react";
import "../style/LandingPage.css";
import DevChat from "./DevChat";

const LandingPage = () => {
  const [openDevChat, setDevChatOpen] = useState(false);

  return (
    <div>
      <header>
        {/* Your header content, such as logo and navigation links */}
        <img src="logo.png" alt="Logo" />
        <nav>
          <a href="#" className="firstNav">Losep</a>
          <a href="#" className="secNav">Rebjis</a>
          <a href="#" className="thirdNav">Masfji</a>
          <a href="#" className="fourthNav">Vajid</a>
        </nav>
      </header>

      <div>
        <button
          className="DevChatButton"
          onClick={() => setDevChatOpen(true)}
        >
          <img src="logo.png" alt="Chat Icon" />
        </button>

        {openDevChat && <DevChat closeDevChat={() => setDevChatOpen(false)} />}
      </div>
    </div>
  );
};

export default LandingPage;
