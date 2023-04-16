import { useState, useEffect } from "react";
import  close  from '../assets/images/close.svg';
import  menu  from '../assets/images/menu.svg';
import { navLinks } from '../constants/index';
import { DatePick } from './DatePick';
// import DatePicker from "react-datepicker";
// import 'react-datepicker/dist/react-datepicker.css'


export const NavBar = (props) => {
    const [active, setActive] = useState(false);
    const [toggle, setToggle] = useState('Home');
    const [startDate, setStartDate] = useState(new Date())
    const [endDate, setEndDate] = useState(new Date())


    const selectStartDate = (date) => {
      setStartDate(date)
    }
    const selectEndDate = (date) => {
      setEndDate(date)
    }

  return (
    <nav className="w-full flex justify-between items-center navbar pt-3">
        <h1 className="text-lime-400 font-medium text-2xl px-5 tracking-tighter">SPOTIFY SONG RANK</h1>
        <ul className="list-none sm:flex hidden jusitfy-end items-center flex-1">
          {navLinks.map((nav, index) => (
            <li
              key={nav.id}
              className={`font-poppings font-nrmal cursor-pointer font-medium text-lg text-[16px] ${index === navLinks.length-1 ? 'mr-0':'mr-8'} text-gray-200 mr-10`}
            >
              <a href={`${nav.id}`}>
                {nav.title}
              </a>
            </li>))}
            <div className="relative flex flex-wrap px-2 -mt-4">
              <div className="font-medium px-4 ">
                <h1 className="text-gray-100 text-center mb-2">Start Date</h1>
                <DatePick selectDate={selectStartDate}/>
              </div>
              <div className= "font-medium px-4 ">
                <h1 className="text-gray-100 text-center mb-2">End date</h1>
                <DatePick selectDate={selectEndDate}/>
              </div>
            </div>
            <div className="px-1 content-center">
                <button type="button" className="bg-slate-700 hover:bg-gray-600 text-slate-300 font-bold py-2 px-3  border-blue-700 rounded"
                onClick={()=> props.select(startDate,endDate)}>
                  GO
                </button>
            </div>
        </ul>

        <div className="inline-flex items-center px-1 py-2.5 text-sm font-medium text-center text-white">
            <img className="h-10 w-10 rounded-full" src={props.data[1]} />
              <div className="px-2 font-sans font-bold text-lg">
                {props.data[0]}
              </div>
        </div>

        
      <div className="sm:hidden flex flex-1 justify-end items-center px-4">
        <img
          src={toggle ? close : menu}
          alt="menu"
          className="w-[28px] h-[28px] object-contain"
          onClick={() => setToggle(!toggle)}
        />

        <div className={`${!toggle ? "hidden" : "flex"} p-8 bg-black absolute top-20 right-0 mx-4 my-0 min-w-[140px] z-50 rounded-xl sidebar`}>
          <ul className="list-none flex justify-end items-start flex-1 flex-col">
            {navLinks.map((nav, index) => (
              <li
                key={nav.id}
                className={`font-poppins font-medium cursor-pointer text-[16px] ${
                  active === nav.title ? "text-white" : "text-gray-500"
                } ${index === navLinks.length - 1 ? "mb-0" : "mb-4"}`}
                onClick={() => setActive(nav.title)}
              >
                <a href={`${nav.id}`}>{nav.title}</a>
                
              </li>
              
            ))}
          </ul>
        </div>
      </div>

    </nav>
    )
  }