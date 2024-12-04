import React from 'react'
import TitleHead from './TitleHead'

function AccountSummary() {

    const [count, setCount] = useState(0);

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
