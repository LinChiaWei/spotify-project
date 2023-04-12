import {React,useState} from 'react';
import { NavBar } from '../../components/Navbar';
import { GetSongs } from '../../api/GetSongs';
import { GetUser } from '../../api/GetUser';
import { SongsList } from '../../components/SongsList';
import styles from '../../styles';


let url = 'http://localhost:8000/'

export const Login = () => {
    const SongsCount = GetSongs(url);
    const UserInfo = GetUser(url); 

    const [startDate, setStartDate] = useState();
    const [endDate, setEndDate] = useState();

    const selectspecificDate = (date) => {
        const SongsCount = GetSongs(url);
    }

    return(
        <div className={`bg-black w-full overflow-hidden`}>
            <div className={`${styles.flexCenter}`}>
                <div className={`w-full bg-gradient-to-r bg-slate-900`}>
                    <NavBar data={UserInfo} selectDate={selectspecificDate}/>
                </div>
            </div>
                <div className={`bg-gradient-to-t bg-slate-900 ${styles.paddingX} ${styles.flexStart}`}>
                    <div className={`${styles.boxWidth}`}>
                        <SongsList data={SongsCount} />
                </div>
            </div>
        </div>
    )
}