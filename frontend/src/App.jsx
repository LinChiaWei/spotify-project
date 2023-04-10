import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css'
import { Login } from './pages/home'
import { ThisMonth } from './pages/thismonth'
import { LastMonth } from './pages/lastmonth'

const App = () => {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="thismonth" element={<ThisMonth />} />
        <Route path="lastmonth" element={<LastMonth />} />
      </Routes>
    </BrowserRouter>
    </>
  ) 
}

export default App;
