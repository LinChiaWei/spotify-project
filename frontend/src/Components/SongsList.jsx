import Grid from '@mui/system/Unstable_Grid';
import { Card,Paper, CardMedia} from '@mui/material';
import React from 'react';

export const SongsList = (props) => {
    return(
        <div className="mt-4 grid grid-cols-2 gap-x-24 gap-y-5 sm:grid-cols-3 lg:grid-cols-4 xl:gap-x-5 drop-shadow-md">
        {props.data.map((item, index) => ( 
          <div className="rounded-lg bg-black bg-opacity-20 object-contain p-3 " >
            <div className="" >
              <div className="tracking-wide text-center font-semibold text-3xl text-red-700 mb-1">
                Rank {index+1}
              </div>
            </div>
            <div className="bg-black static ">                  
              <img className="aspect-square object-contain rounded-sm" src={item[1]}/>
            </div>
            <div className="p-2">
              <div className="tracking-wide font-center font-bold text-gray-100 truncate">
                {item[0]}
              </div>
            </div>
            <div className="pt-2 px-2">
              <div className="tracking-tight pt-2 pb-3 font-center text-sm text-gray-300 font-mono">
                Song Count: {item[2]}
              </div>
            </div>
          </div>
          ))}
        </div>
    )
}