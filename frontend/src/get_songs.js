import { useState, useEffect } from "react";

export function GetSongs(url) {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function getData() {
            const headers = { 
                'Content-Type': 'application/json',
            };
    
            const response = await fetch(`${url}`, { 
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
