import React from 'react';
import styles from '../styles'
import sad_img from '../assets/images/sad.gif'


export const renderDefaultPage = () => {
    return (
        <div className={`bg-auto ${styles.boxWidth} mt-4`}>    
            <div className={`bg-gradient-to-t bg-slate-900 ${styles.flexStart} mb-4` }>
                <div className={`text-4xl my-24 text-red-700 font-semibold`}>
                    DATA NOT FOUND
                </div>
            </div>
            <div className={` ${styles.flexCenter} mb-72`}>
                <img src={sad_img} alt="Loading Animation"/>
            </div>
            <div>
                <div className={`from-inherit`}>
                    
                </div>
            </div>
        </div>
    );
  };