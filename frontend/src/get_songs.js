import { useState, useEffect } from "react";

export function GetSongs(url) {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function postData(url) {
            const headers = { 
                'Content-Type': 'application/json',
            };
    
            const res = await fetch(`${url}/`, { 
                headers: headers,
                method: 'POST',
            })
            .then(response => response.json())
            .catch(error => console.error('Error:', error))
            .then(response => console.log('Success:', response))

            const data = await res.json();
            postData(data["message"]);
        }
        postData();
    }, []);
    return data;
}
