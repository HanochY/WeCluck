import { useState } from "react";

const RegistrationForm = ({registrationCallback}) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const onSubmit = async (e) => {
        e.preventDefault()
        if(password === confirmPassword){
            const data = {
                username,
                password
            }
            const url = "http://127.0.0.1:5000/user"
            const options = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
            const response = await fetch(url, options)
            if (response.status !== 201 && response.status !== 200) {
                const data = await response.json()
                registrationCallback(data.message, false)
            } else {
                registrationCallback(data.message, true) ///in login page make function which updates paragraph with success or fail and pass here
            }
        } else {
            registrationCallback("Passwords do not match!", false)
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    onChange={(e) => setUsername(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="confirmPassword">Confirm Password:</label>
                <input
                    type="password"
                    id="confirmPassword"
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default RegistrationForm
