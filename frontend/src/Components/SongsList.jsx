import { TbCurrentLocation } from 'react-icons/tb';
import { RiSuitcaseLine } from 'react-icons/ri';
import { RiMoneyDollarCircleFill } from 'react-icons/ri';
import Table from 'react-bootstrap/Table'
import  { Button,Container, textFieldClasses} from '@mui/material'
// import { Container } from 'react-bootstrap';
import React from 'react';
import { Link } from 'react-router-dom';


export const SongsList = (props) => {
  // console.log(props.data)
  // var str = JSON.stringify(props.data);
  // const theme = useTheme();

    return(
      <Container>
        <Button variant="text">
          Text
        </Button>
      </Container>
      
        // <div>
        //   <Table striped bordered hover variant="dark">
        //     <thead>
        //       <tr>
        //         <th> </th>
        //         <th>Song Name</th>
        //         <th>Listen Rank</th>
        //       </tr>
        //     </thead>
        //     {props.data.map(item => (
        //       <tbody key={item[0]}>
        //         <tr>
        //           <td><img style={{ height:150, width:150}} src={item[1]}></img></td>
        //           <td>{item[0]}</td>
        //           <td>{item[2]}</td>
        //         </tr>
        //       </tbody>
        //   ))}
        //   </Table>
        // </div>


        // <div className="flex flex-col w-[250px] p-4 bg-white/5 bg-opacity-80 backdrop-blur-sm animate-slideup rounded-bg cursor-pointer">
        //     {props.data.map(item => (
        //       <img style={{ height:150, width:150}} src={item[1]}></img>


        //   ))}
          
        // </div>

    );
}