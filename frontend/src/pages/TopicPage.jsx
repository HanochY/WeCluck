import { useState } from "react";

import TopicAddForm from '../components/TopicAddForm';
import TopicRemoveButton from '../components/TopicRemoveButton';
import TopicList from '../components/TopicList';

function TopicPage() {
    const [messageBox, setMessageBox] = useState("")
    const redirectToCommentPage = (message) => {
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

export default TopicPage
