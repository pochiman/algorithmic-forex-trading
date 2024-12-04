import React, { useState } from 'react';
import { GRANULARITIES, PAIRS } from '../app/data';
import Button from '../components/Button';
import Select from '../components/Select';
import TitleHead from '../components/TitleHead';

function Dashboard() {

    const [ selectedPair, setSelectedPair ] = useState(PAIRS[0].value)
    const [ selectedGran, setSelectedGran ] = useState(GRANULARITIES[0].value)

    return (
        <div>
            <TitleHead title="Options" />
            <div className="segment options">
                <Select
                    name="Currency"
                    title="Select currency"
                    options={PAIRS}
                    defaultValue={selectedPair}
                    onSelected={setSelectedPair}
                />
                <Select
                    name="Granularity"
                    title="Select granularity"
                    options={GRANULARITIES}
                    defaultValue={selectedGran}
                    onSelected={setSelectedGran}
                />
                <Button text="Load" handleClick={undefined} />
            </div>    
        </div>
    )
}

export default Dashboard
