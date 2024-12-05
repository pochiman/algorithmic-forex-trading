import React from 'react'

const HEADERS = [
    "R1", "R2", "R3",
    "S1", "S2", "S3",
    "pivot"
];

function Technicals({ data }) {
    return (
        <div className='segment'>
            <table>
                <thead>
                    <tr>{
                        HEADERS.map(item => {
                            return <th key={item}>{item}</th>
                        })
                    }
                    </tr>
                    <tr>{
                        HEADERS.map(item => {
                            return <td key={item}>{data[item]}</td>
                        })
                    }
                    </tr>
                </thead>    
            </table>    
        </div>
    )
}

export default Technicals
