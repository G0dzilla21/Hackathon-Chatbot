import React, { useState } from "react";
import "../style/Login.css";

const Register = () => {
    const [email, setEmail] = useState("")
    const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [successMessage, setSuccessMessage] = useState("");
	const [errorMessage, setErrorMessage] = useState("");
    
	const handleRegister = async () => {
		const requestObject = {
            username: username,
            email: email,
			password: password,
		};

		try {
			const response = await fetch("http://localhost:8080/signup", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(requestObject),
			});

			if (response.ok) {
				const data = await response.json();
				const { csrf_token } = data;
				localStorage.setItem("csrf_token", csrf_token);
				localStorage.setItem("username", username);
				console.log("You would have been successful if this was linked.")
			} else {
				setSuccessMessage("");
				setErrorMessage("Registation failed. .");
			}
		} catch (error) {
			console.log(error);
			setSuccessMessage("");
			setErrorMessage("An error occurred. Please try again.");
		}
        
	};

    return (
        <div className="login-container">

        <h1 className="center">Register a new Account</h1>
            <div className="login-text-container">		

              <div className="loginBox">
                    <label htmlFor="username">Username</label>
                    <br />
                    <input className="addedInfo"
                        type="text"
                        id="Username"
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>

                <div className="loginBox">
                    <label htmlFor="username">Email</label>
                    <br />
                    <input className="addedInfo"
                        type="text"
                        id="Email"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>		

                <div className="loginBox">
                    <label htmlFor="password">Password</label>
                    <br />
                    <input className="addedInfo"
                        type="password"
                        id="Password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <br/>

                <div className="centerBtn">
                    <button onClick={handleRegister}>
                    Register
                    </button>
                    <br/>
                    <button>Back</button>
                </div>
                <br/>

                {successMessage && (
                    <p className="center" style={{ color: "green" }}>{successMessage}</p>
                )}
                {errorMessage && <p className="center">{errorMessage}</p>}
            </div>
        </div>
    );
};

export default Register;