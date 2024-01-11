import { useState } from "react";

import "../style/LandingPage.css";
import DevChat from "./DevChat";

const LandingPage = () => {
  const [openDevChat, setDevChatOpen] = useState(false);
  return (
    <div>
      <header>
        <img src="logo.png" alt="Italian Trulli" className="logodes" />
        <nav>
          <a href="#" className="firstNav">
            About
          </a>
          <a href="#" className="secNav">
            Products
          </a>
          <a href="#" className="thirdNav">
            Login
          </a>
          <a href="#" className="fourthNav">
            Register
          </a>
        </nav>
      </header>

      <div className="cards">
        <h2>
          <b>About</b>
        </h2>
        <h4>
          Ferestha is next Gen AI chat bot that uses Chat GPT's OpenAPI in order
          to create an interactive Database Developer Guide
        </h4>
      </div>

      <div className="cards">
        <h2>
          <b>Suggestions</b>
        </h2>
        <h4>How Do I create A database?</h4>
        <h4>Which database should I create?</h4>
        <h4>Create a Schema?</h4>
        <h4>Create a database?</h4>
      </div>

      <div>
        <div className="ModalButton">
          <button
            className="DevChatButton"
            onClick={() => {
              setDevChatOpen(true);
            }}
          >
            <img src="logo.png" alt="Italian Trulli" />
          </button>
        </div>
        {openDevChat && <DevChat closeDevChat={setDevChatOpen} />}
      </div>
    </div>
  );
};

export default LandingPage;
