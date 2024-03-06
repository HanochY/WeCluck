import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  const [count, setCount] = useState(0)

  return (
      <div class="horizontal-forms-div">
        <form class="vertical-form" method="post" id="register">
          <h1 class="signin-signup-title">Sign Up</h1>
          <label for="register_username">Username</label>
          <input class="input" type="text" id="register_username" name="register_username"/>
          <label for="register_password">Password</label>
          <input class="input" type="password" id="register_password" name="register_password"/>
          <label for="confirm_register_password">Confirm Password</label>
          <input class="input" type="password" id="confirm_register_password" name="confirm_register_password"/>
          <input class="button" type="submit" name="button" value="register"/>
        </form>
        <form class="vertical-form" method="post" id="login">
          <h1 class="signin-signup-title">Sign In</h1>
          <label for="login_username">Username</label>
          <input class="input" type="text" id="login_username" name="login_username"/>
          <label for="login_password">Password</label>
          <input class="input" type="password" id="login_password" name="login_password"/>
          <input class="button" type="submit" name="button" value="login"/>
        </form>
      </div>
  )
}

export default App
