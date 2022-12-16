import { useState, useEffect } from "react";

export function GetSongs(url) {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function getData(url) {
            const headers = { 
                'Content-Type': 'application/json',
            };
            const response = await fetch(`${url}/`, { 
                headers: headers,
                method: 'POST',
            });
            // .then(response => response.json())
            // .catch(error => console.error('Error:', error))
            // .then(response => console.log('Success:', response))

            const content = await response.json();
            setData(content);
        }
        getData();
    }, []);
    return data;
}
