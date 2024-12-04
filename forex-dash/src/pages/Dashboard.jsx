import React, { useState } from 'react';
import { PAIRS } from '../app/data';
import Select from '../components/Select';
import TitleHead from '../components/TitleHead';

function Dashboard() {

    const [ selectedPair, setSelectedPair ] = useState(PAIRS[0].value)

    return (
        <div>
            <TitleHead title="Options" />
            {setSelectedPair}
            <div className="segment options">
                <Select
                    name="Currency"
                    title="Select currency"
                    options={PAIRS}
                    defaultValue={selectedPair}
                    onSelected={setSelectedPair}
                />    
            </div>    
        </div>
    )
}

export default Dashboard
