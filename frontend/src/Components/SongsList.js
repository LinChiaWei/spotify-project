import { TbCurrentLocation } from 'react-icons/tb';
import { RiSuitcaseLine } from 'react-icons/ri';
import { RiMoneyDollarCircleFill } from 'react-icons/ri';
import styles from '../styles';
import Table from 'react-bootstrap/Table'


export const SongsList = (props) => {
  console.log(props.data)
  // var str = JSON.stringify(props.data);
    return(
        <div>
          <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th> </th>
                <th>Song Name</th>
                <th>Listen Rank</th>
              </tr>
            </thead>
            {props.data.map(item => (
              <tbody>
                <tr>
                  <td><img style={{ height:150, width:150}} src={item[1]}></img></td>
                  <td>{item[0]}</td>
                  <td>{item[2]}</td>
                </tr>
              </tbody>
          ))}
          </Table>
        </div>
    );
}