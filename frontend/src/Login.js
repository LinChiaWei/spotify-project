import React, { useEffect, useState } from 'react';
import { Container, Form, Button, Nav } from 'react-bootstrap';
import { NavBar } from './Components/Navbar'

let url = 'http://127.0.0.1:8000'

export default function Login() {


    function postData(url) {

        fetch(`${url}/`)
            .then((response) => response.json())
            .then((result) => console.log(result))
            .catch((error) => console.log('error', error))
    }

    return(
        <Container className="align-items-center d-flex" sytle={{ height:'100vh'}}>
            <div>
                {/* <a className="title">Spotify Songs List</a> */}
                <NavBar />
            </div>
            <div>
                <Button onClick={() => {postData(url)}}> Click It !!!</Button>
            </div>


            {/* <Form>
                <Form.Group className='mb-3' controlId="formId">
                <Form.Label>Account ID</Form.Label>
                <Form.Control type="Id" placeholder="Enter ID" />
                <Form.Text className="text-muted"></Form.Text>
                </Form.Group>

                <Form.Group className='mb-3' controlId="formpassward">
                <Form.Label>Account passward</Form.Label>
                <Form.Control type="Id" placeholder="Enter Passward" />
                <Form.Text className="text-muted"></Form.Text>
                </Form.Group>
                <Button type="submit" clasName="mr-2">Login</Button>
            </Form> */}
        </Container>
    )
}