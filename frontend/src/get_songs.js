import { useState, useEffect } from "react";

export function GetSongs(url) {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function getData(url) {
            const headers = { 
                'Content-Type': 'application/json',
            };
    
            const response = await fetch('http://127.0.0.1:8000/', { 
                headers: headers,
                method: 'GET',
            });

            const data = await response.json();
            setData(data["message"]);
        }
        getData();
    }, []);
    return data;
}
