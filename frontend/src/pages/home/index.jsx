import React, { useState, useEffect } from 'react';
import { NavBar } from '../../components/Navbar';
import { SongsList } from '../../components/SongsList';
import styles from '../../styles';
import { FaArrowCircleUp } from 'react-icons/fa';

let url = 'http://localhost:8000/'

export const Login = () => {

    const [songs, setSongs] = useState([]);
    const [userInfo, setUserInfo] = useState([]);
    const [Start, setStart] = useState("");
    const [End, setEnd] = useState("");

    const dateTransform = (date) => {
        let year = date.getFullYear();
        let month = date.getMonth() + 1;
        let dt = date.getDate();
        let dateString = `${year}-${month}-${dt}`;
        return dateString;
    }

    const songsApi = async(url, dateString) => {
        const response  = await fetch(`${url}${dateString}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },    
        })
        const data = await response.json();
        return data;
    }

    const selectspecificDate = (sdate,edate) => {
        sdate = new Date(sdate);
        edate = new Date(edate);
        const startDate = dateTransform(sdate);
        const endDate = dateTransform(edate);

        setStart(startDate);
        setEnd(endDate);

        console.log(startDate, endDate)

        let dateString = '';
        if(sdate && edate){
            dateString = `?start_date=${encodeURIComponent(startDate)}&end_date=${encodeURIComponent(endDate)}`
        }

        songsApi(url, dateString)
        .then(data => {
            setSongs(data["message"]);
            setUserInfo(data["user_info"]);
        }).catch(error => {
            console.error(error);
        });
    }

    useEffect(() => {
        songsApi(url, '')
        .then(data => {
            setSongs(data["message"]);
            setUserInfo(data["user_info"]);
        }).catch(error => {
            console.error(error);
        });
    }, []);

    return(
        <div className={`bg-black w-full overflow-hidden`}>
            <div className={`w-full fixed z-20 ${styles.flexCenter}`}>
                <div className={`w-full bg-slate-900`}>
                    <NavBar data={userInfo} select={selectspecificDate}/>
                </div>
            </div>
                {/* <div className='px-5 bg-slate-900'>
                    <p className='text-white font-medium text-2xl'>
                        {Start} {"~ "+End}
                    </p>
                </div> */}
                <div className={`pt-24 bg-gradient-to-t from-slate-900 bg-slate-900/75 ${styles.paddingX} ${styles.flexStart}`}>
                    <div className={` ${styles.boxWidth}`}>
                        <SongsList data={songs} />
                </div>
            </div>
        </div>
    )
}