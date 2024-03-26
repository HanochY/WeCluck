import { useState } from 'react'
import './App.css'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import LoginPage from './pages/LoginPage';

function App() {
    const [messageBox, setMessageBox] = useState("")
    return (
        <>
            <LoginPage/>
        </>
      
    )
}

export default App
