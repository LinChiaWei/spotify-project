import React, {useState} from "react";
import DatePicker from "react-datepicker";
import 'react-datepicker/dist/react-datepicker.css'



export const DatePick = (props) => {
    const [date, setDate] = useState(null);

    return(
        <div>
        <DatePicker 
            dateFormat="dd/MM/yyyy"
            selected = {date}
            onChange={(date) => {
                setDate(date)
                props.selectDate(date)
            }}
        />
        </div>
        // <input type="date" onChange={e=>props.Date=e.target.value} />
    )
}
