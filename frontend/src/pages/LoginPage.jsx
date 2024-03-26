import { useState } from "react";

import LoginForm from '../components/LoginForm';
import RegistrationForm from '../components/RegistrationForm';

function LoginPage() {
    const [messageBox, setMessageBox] = useState("")
    const onLogin = (message, isSuccessful) => {
        if(isSuccessful){
            alert(message)
            //move to next page
        }
        else{
            setMessageBox(message)
        }
    }
    const onRegister = (message, isSuccessful) => {
        if(isSuccessful){
            setMessageBox(message)
        }
        else{
            setMessageBox(message)
        }
    }
    return (
        <>
            <RegistrationForm registrationCallback={onRegister}/>
            <LoginForm loginCallback={onLogin}/>
            <p id='messageBox'>
                {messageBox}
            </p>
        </>
      
    )
}

export default LoginPage
