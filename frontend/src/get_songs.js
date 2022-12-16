import { useState, useEffect } from "react";

export function GetSongs(url) {
    const [list, setData] = useState([]);

    useEffect(() => {
<<<<<<< HEAD
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
=======
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
>>>>>>> a9b7955f819bf3d2933b2bccfd0e94c68fa9046c
        }
        getData();
    }, []);
    return list;
}
