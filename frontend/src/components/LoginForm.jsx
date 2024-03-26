import { useState } from "react";

const LoginForm = ({loginCallback}) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const onSubmit = async (e) => {
        e.preventDefault()
        const url = "http://127.0.0.1:5000/users/"
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "username": username,
                "password": password
            })
        }
        const response = await fetch(url, options)
        const data = await response.json()
        if (response.status !== 201 && response.status !== 200) {
            loginCallback(data.message, false)
        } else {
            sessionStorage.setItem("bearerToken", response.data.token)
            loginCallback(data.message, true) ///in login page make function which updates paragraph with success or fail and pass here
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
            <button type="submit">Register</button>
        </form>
    );
};

export default LoginForm
