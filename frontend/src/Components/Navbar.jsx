
import { useState, useEffect } from "react";
import  close  from '../assets/images/close.svg';
import  menu  from '../assets/images/menu.svg';
import { navLinks } from '../constants/index';


export const NavBar = (props) => {
    const [active, setActive] = useState(false);
    const [toggle, setToggle] = useState('Home');

  return (
    <nav className="w-full flex py-6 justify-between items-center navbar">
        <h1 className="text-lime-500 font-medium text-xl px-5">SPOTIFY SONG RANK</h1>
        <ul className="list-none sm:flex hidden jusitfy-end item- flex-1">
          {navLinks.map((nav, index) => (
            <li
              key={nav.id}
              className={`font-poppings font-nrmal cursor-pointer font-medium text-[16px] ${index === navLinks.length-1 ? 'mr-0':'mr-10'} text-white mr-10`}
            >
              <a href={`${nav.id}`}>
                {nav.title}
              </a>
            </li>))}
        </ul>
        
        <div className="ml-4 flex-2">
            <a className="font-medium text-indigo-600 hover:text-indigo-500">
              <img className="h-8 w-8 rounded-full" src={props.data[1]} alt="" />
              <div>{props.data[0]}</div>
            </a>
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