import React, { useRef } from 'react';
import { Container, Form, Button } from 'react-bootstrap';


const AUTH_URL = "https://accounts.spotify.com/authorize?client_id=a5f4717d6cbe43fea2cc354da04490b6&response_type=code&redirect_uri=http://localhost:8888/callback&scope=user-read-recently-played"

export default function Login() {


    return(
        <Container className="align-items-center d-flex" sytle={{ height:'100vh'}}>
            <Form>
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
                <Button type="submit" clasName="mr-2" href={AUTH_URL}>Login</Button>
            </Form>
        </Container>
    )
}