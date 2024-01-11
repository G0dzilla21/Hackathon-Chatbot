import axios from "axios";
import { useState } from "react";
import Form from "react-bootstrap/Form";
import "../style/Chat.css";
import useCookie from "./hooks/useCookie";

const Chat = () => {
  const [textInput, setTextInput] = useState("");
  const [chat, setChat] = useState([]);
  const [basePath, setBasePath] = useState(
    "C:\\Users\\joshu_yu92ohr\\Desktop\\HACKT\\Gen_AI_Hackathon_Project\\backend"
  );

  const { getCookie } = useCookie(); // Use the useCookie hook
  const csrfToken = getCookie("localhost"); // Replace 'csrf_token' with the actual name of your CSRF cookie

  const axiosInstance = axios.create({
    baseURL: "http://localhost:5000/",
    headers: {
      "Content-Type": "application/json",
      //withCredentials : true,
      "X-CSRFToken": csrfToken, // Add CSRF token to the request headers
    },
  });

  const interact = async () => {
    try {
      console.log(chat);
      console.log(textInput);
      const response = await axiosInstance.post("api/ask-openai", {
        user_input: textInput,
        // chat: chat.map((item) => item.text), // Extract user messages
      });

      const userMessage = { role: "user", text: textInput };
      const aiMessage = { role: "AI", text: response.data.response }; // Assuming 'response.data.response' contains the AI's response

      setChat([...chat, userMessage, aiMessage]);
      setTextInput("");
      console.log(textInput);
      console.log(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="main">
      <div className="convDisplay">
        <h2>Hi! I'm Ferestha</h2>
        <div className="chatLog">
          {chat.map((item, index) => (
            <div
              key={index}
              style={{
                backgroundColor: index % 2 === 0 ? "#DFDFDF" : "#000",
                color: index % 2 === 0 ? "black" : "white",
                textAlign: index % 2 === 0 ? "right" : "left",
                marginBottom: "20px",
                whiteSpace:
                  "pre-wrap" /* whiteSpace: 'pre-wrap' must be here for formatting */,
              }}
            >
              <p>
                <strong>{item.role}: </strong>
                {item.text}
              </p>
            </div>
          ))}
          <Form>
            <Form.Group>
              <Form.Control
                as="textarea"
                rows={2}
                value={textInput}
                placeholder="Type here..."
                onChange={(e) => setTextInput(e.target.value)}
                style={{ resize: "none", color: "black" }}
              ></Form.Control>
              <div>
              <button type="button" onClick={interact}>
                Submit
              </button>
              </div>
            </Form.Group>
          </Form>
        </div>
      </div>
    </div>
  );
};

export default Chat;
