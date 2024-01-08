import "../style/LandingPage.css";
import Chat from "./Chat";

const LandingPage = () => {
  return (
    <div>
      <header>
        <img src="logo.png" alt="Italian Trulli" />
        <nav>
          <a href="#">Login</a>
          <a href="#">Register</a>
        </nav>
      </header>
      <Chat />
    </div>
  );
};

export default LandingPage;
