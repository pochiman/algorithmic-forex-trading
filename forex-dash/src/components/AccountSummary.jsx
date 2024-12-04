import React, { useEffect, useState } from 'react'
import endPoints from '../app/api';
import TitleHead from './TitleHead'

function AccountSummary() {

    const [account, setAccount] = useState(null);

    useEffect(() => {
        loadAccount();
    }, [])

    const loadAccount = async () => {
        const data = await endPoints.account();
        setAccount(data);
    }

    return (
        <div>
            <TitleHead title="Account Summary" />
            {
                account && <div>
                    <pre>{JSON.stringify(account, null, 2)}</pre>
                </div>
            }
        </div>
    )
}

export default AccountSummary
