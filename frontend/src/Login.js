import React, { useEffect, useState } from 'react';
import { Container, Form, Button, Nav, Table } from 'react-bootstrap';
import { NavBar } from './Components/Navbar'
import { GetSongs } from './get_songs'
import { SongsList } from './Components/SongsList'
import styles from './styles'

let url = 'http://127.0.0.1:8000'

export const Login = () => {
    const SongsCount = GetSongs(url);
    // for(var i in GetSongs(url))
    // var str = JSON.parse(SongsCount);

    // var str = JSON.stringify(SongsCount, null, 2);
    // console.log(str)

    return(
        <div>
            <div className="navbar">
                <NavBar />
            </div>

            <div className={`bg-primary ${styles.paddingX} ${styles.flexCenter}`}>
                <div className={`${styles.boxWidth}`}>
                <SongsList data={SongsCount} />

                </div>
            </div>
      
        </div>
    )
}