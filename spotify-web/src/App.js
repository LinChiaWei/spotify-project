
import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import Login from './Login'

function App() {
  const [id, setId] = useState()


  return (
    <>
      {id}
      <Login onIdSubmit={setId}/>
    </>
  ) 
}

export default App;
