import React from 'react';
import { Container, Form, Nav, Table } from 'react-bootstrap';
import { NavBar } from './Components/Navbar'
import { GetSongs } from './get_songs'
import { SongsList } from './Components/SongsList'
import styles from './styles'
import { Box, Grid, Button} from '@mui/material'

let url = 'http://127.0.0.1:8000'

export const Login = () => {
    const SongsCount = GetSongs(url);

    return(
        <div>
            <div className="navbar">
                <NavBar />
            </div> 
            <div>
                <div >
                <SongsList data={SongsCount} />
                </div>
            </div>
        </div>
    )
}