import { useState, useEffect } from "react";

export function GetUser(url) {
    const [list, setData] = useState([]);

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
            setData(data["user_info"]);
        }
        getData();
    }, []);
    return list;
}