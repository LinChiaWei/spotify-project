import React from 'react';


// write the code to show the rank of genres in list 
export const Genres = (props) => {
    return (
        <div className="mt-4 mb-4 drop-shadow-md overflow-x-auto">
            <table className="min-w-full bg-gray-800 rounded-lg">
                <thead>
                    <tr>
                        <th className="py-3 px-6 border-b-2 border-gray-700 text-red-500 text-xl font-semibold text-center">
                            Rank
                        </th>
                        <th className="py-3 px-6 border-b-2 border-gray-700 text-gray-300 text-xl font-semibold text-center">
                            Genre Name
                        </th>
                        <th className="py-3 px-6 border-b-2 border-gray-700 text-gray-300 text-xl font-semibold text-center">
                            Count
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {props.data.map((item, index) => (
                        <tr key={item[0]} className="hover:bg-gray-700 transition-colors">
                            <td className="py-3 px-6 border-b border-gray-700 text-center text-gray-100 text-lg">
                                {index + 1}
                            </td>
                            <td className="py-3 px-6 border-b border-gray-700 text-center text-gray-100 text-lg truncate">
                                {item[0]}
                            </td>
                            <td className="py-3 px-6 border-b border-gray-700 text-center text-gray-300 text-lg">
                                {item[1]}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}
