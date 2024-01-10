import { useState } from "react";

import "../style/LandingPage.css";
import DevChat from "./DevChat";

const LandingPage = () => {
  const [openDevChat, setDevChatOpen] = useState(false);
  return (
    <div>
      <header>
        <img src="logo.png" alt="Italian Trulli" />
        <nav>
          <a href="#" className="firstNav">
            Losep
          </a>
          <a href="#" className="secNav">
            Rebjis
          </a>
          <a href="#" className="thirdNav">
            Masfji
          </a>
          <a href="#" className="fourthNav">
            Vajid
          </a>
        </nav>
      </header>

      <div>
        <button
          className="DevChatButton"
          onClick={() => {
            setDevChatOpen(true);
          }}
        >
          <img src="logo.png" alt="Italian Trulli" />
        </button>
        {openDevChat && <DevChat closeDevChat={setDevChatOpen} />}
      </div>
    </div>
  );
};

export default LandingPage;
