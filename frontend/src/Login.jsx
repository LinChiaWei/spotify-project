import React from 'react';
import { NavBar } from './Components/Navbar'
import { GetSongs } from './get_songs'
import { SongsList } from './Components/SongsList'


let url = 'http://localhost:8000'

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