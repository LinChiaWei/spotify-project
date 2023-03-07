
import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css'
import { Login } from './Login'
import './App.css'
// import  { Button, Container, Grid, Paper } from '@mui/material'
// import { styled } from '@mui/system';



const App = () => {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
      </Routes>
    </BrowserRouter>
    </>
  ) 
}

export default App;
