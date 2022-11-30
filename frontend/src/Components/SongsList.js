import { TbCurrentLocation } from 'react-icons/tb';
import { RiSuitcaseLine } from 'react-icons/ri';
import { RiMoneyDollarCircleFill } from 'react-icons/ri';
import styles from '../styles';

export const SongsList = (props) => {
    return(
        <div>
          {props.data.map(item => (<h2> Songs Name: {item[0]} </h2> ))}
        </div>
    )
}