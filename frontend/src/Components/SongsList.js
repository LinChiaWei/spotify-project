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
          <Table striped>
            <thead>
              <tr>
                <th>SongName</th>
                <th>ListenCount</th>
              </tr>
            </thead>
            {props.data.map(item => (
              <tbody>
                <tr>
                  <td>{item[0]}</td>
                  <td>{item[1]}</td>
                </tr>
              </tbody>
          ))}
          </Table>
        </div>
    );
}