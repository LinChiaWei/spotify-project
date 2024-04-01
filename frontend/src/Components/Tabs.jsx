import React, { useState } from 'react';

export const Tabs = ({ currentTab, onTabChange }) =>{

    const handleTabClick = (tabName) => {
        onTabChange(tabName);
    };

    return (
        <div className="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700">
            <ul className="flex flex-wrap -mb-px">
                <li className="me-2">
                    <a href="#" className={`inline-block p-4 border-b-2 border-transparent rounded-t-lg ${currentTab === 'Song' ? 'hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300' : ''}`} onClick={() => handleTabClick('Song')} aria-current={currentTab === 'Song'}>Song</a>
                </li>
                <li className="me-2">
                    <a href="#" className={`inline-block p-4 border-b-2 border-transparent rounded-t-lg ${currentTab === 'Artist' ? 'hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300' : ''}`} onClick={() => handleTabClick('Artist')} aria-current={currentTab === 'Artist'}>Artist</a>
                </li>
                <li className="me-2">
                    <a href="#" className={`inline-block p-4 border-b-2 border-transparent rounded-t-lg ${currentTab === 'Genre' ? 'hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300' : ''}`} onClick={() => handleTabClick('Genre')} aria-current={currentTab === 'Genre'}>Genre</a>
                </li>
            </ul>
        </div>
    );
};