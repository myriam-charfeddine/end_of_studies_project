import React from 'react';
// import ReactDOM from 'react-dom/client';
import './index.css';
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import './Components/System_buttons'



ReactDOM.render(
  <BrowserRouter>
    <system-web-comp/>
  </BrowserRouter>,
  document.getElementById("root")
);

