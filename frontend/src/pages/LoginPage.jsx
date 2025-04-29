import { useState } from "react";

import LoginForm from '../components/LoginForm';
import RegistrationForm from '../components/RegistrationForm';

function LoginPage() {
    const [messageBox, setMessageBox] = useState("")
    const redirectToHomepage = (message) => {
            setMessageBox(message)
    }
    return (
        <>
            <RegistrationForm successCallback={setMessageBox} failureCallback={setMessageBox}/>
            <LoginForm successCallback={redirectToHomepage} failureCallback={setMessageBox}/>
            <p id='messageBox'>
                {messageBox}
            </p>
        </>
      
    )
}

export default LoginPage
