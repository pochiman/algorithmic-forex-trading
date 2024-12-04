import React, { useEffect, useState } from 'react'
import endPoints from '../app/api';
import TitleHead from './TitleHead'

function Headlines() {

    const [headlines, setHeadlines] = useState(null);

    useEffect(() => {
        loadHeadlines();
    }, [])

    const loadHeadlines = async () => {
        const data = await endPoints.headlines();
        setHeadlines(data);
    }
    return (
        <div>
            <TitleHead title="Headlines" />
            <div className="segment">
                {
                    headlines && headlines.map((item, index) => {
                        return <div key= {index}>{item.headline}</div>
                    })
                }
            </div>
        </div>
    )
}

export default Headlines
