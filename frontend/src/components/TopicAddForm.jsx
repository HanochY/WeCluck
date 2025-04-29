import { useState } from "react";

const TopicAddForm = ({successCallback, failureCallback}) => {
    const [newUsername, setNewUsername] = useState("");
    const [newPassword, setNewPassword] = useState("");
    const [confirmNewPassword, setConfirmNewPassword] = useState("");

    const onSubmit = async (e) => {
        e.preventDefault()
        if(newPassword !== confirmNewPassword){
            registrationCallback("Passwords do not match!", false)
        } else {
            const url = "http://127.0.0.1:5000/comments/"
            const options = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Request": "POST",
                    "Access-Control-Allow-Headers": "X-Requested-With"
                },
                body: JSON.stringify({
                    "username": newUsername,
                    "password": newPassword
                })
            }
            const response = await fetch(url, options)
            const data = await response.json()
            if (response.status !== 201 && response.status !== 200) {
                successCallback(data.error, false)
            } else {
                failureCallback(data.message, true) ///in login page make function which updates paragraph with success or fail and pass here
            }
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="newUsername">Username:</label>
                <input
                    type="text"
                    id="newUsername"
                    onChange={(e) => setNewUsername(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="newPassword">Password:</label>
                <input
                    type="password"
                    id="newPassword"
                    onChange={(e) => setNewPassword(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="confirmNewPassword">Confirm Password:</label>
                <input
                    type="password"    
                    id="confirmNewPassword"     
                    onChange={(e) => setConfirmNewPassword(e.target.value)}
                />
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default TopicAddForm
