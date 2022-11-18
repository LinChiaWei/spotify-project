import React, { useEffect, useState } from 'react';
import { Container, Form, Button, Nav, Table } from 'react-bootstrap';
import { NavBar } from './Components/Navbar'
import { GetSongs } from './get_songs'

let url = 'http://127.0.0.1:8000'

export default function Login() {

    return(
        <Container className="outside">
            <div className="navbar">
                {/* <a className="title">Spotify Songs List</a> */}
                <NavBar />
            </div>
            <div className="mb-2">
                <Button onClick={() => {GetSongs(url)}}> Click It !!!</Button>
            </div>

            {/* <Table strpied borderd hover vareiant="dark">
                
            </Table> */}


            
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