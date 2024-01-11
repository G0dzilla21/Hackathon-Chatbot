import axios from 'axios';
import React, { useEffect, useRef, useState } from 'react';
import Modal from 'react-modal';
import '../style/Chat.css'; // Ensure this path is correct

Modal.setAppElement('#root'); // This is important for accessibility

const Chat = ({ closeChat }) => {
    const [textInput, setTextInput] = useState('');
    const [chat, setChat] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const chatEndRef = useRef(null);

    const axiosInstance = axios.create({
        baseURL: 'http://localhost:5000/',
        headers: {
            'Content-Type': 'application/json',
        }
    });

    const interact = async () => {
        if (!textInput.trim()) return; // Prevent sending empty messages
        setIsLoading(true);
        try {
            const response = await axiosInstance.post('api/ask-openai', {
                user_input: textInput,
            });

            const userMessage = { role: "user", text: textInput };
            const aiMessage = { role: "AI", text: response.data.response };

            setChat([...chat, userMessage, aiMessage]);
            setTextInput('');
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            interact();
        }
    };

    const scrollToBottom = () => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [chat, isLoading]);

    return (
        <Modal 
            isOpen={true}
            onRequestClose={closeChat}
            className="Modal"
            overlayClassName="Overlay"
        >
            <div className="chatInterface">
                <button onClick={closeChat} className="closeButton">X</button>
                <h1 style={{ color: 'black' }}>Chat with AI</h1>
                
                <div className="chatLog">
                <h4 style={{ color: 'black' }}>chatbot: How can I help?</h4>
                    {chat.map((item, index) => (
                        <div key={index} className={`chat-message ${item.role}`} style={{ whiteSpace: 'pre-wrap', color: 'black' }}>
                            <p><strong>{item.role === 'user' ? 'User' : 'Chatbot'}:</strong> {item.text}</p>
                        </div>
                    ))}
                    
                    {isLoading && <p className="thinking">Thinking...</p>}
                    
                    <div ref={chatEndRef} />
                </div>
                <br></br>
                <textarea 
                    value={textInput} 
                    onChange={(e) => setTextInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder=" Type your message here..."
                />
                <br></br>
                <button onClick={interact} className="sendButton">Send</button>
            </div>
        </Modal>
    );
};

export default Chat;