import React, { useEffect, useState } from 'react'
import TitleHead from './TitleHead'

function AccountSummary() {

    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log("Rendered", count);
    }, [])

    const handleIncr = () => {
        setCount(count + 1);
    }

    return (
        <div>
            <TitleHead title="Account Summary" />
            <button onClick={() => handleIncr()}>Incr</button>
            <div>{count}</div>
        </div>
    )
}

export default AccountSummary
