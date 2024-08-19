import React from 'react';
import Btn from 'components/Btn';
import { get } from 'src/fetch';

export default function ToggleLeds() {
    return <Btn onClick={() => {
        get('/toggleLeds')
            .then(res => console.log(res))
    }}
    >
        toggle Leds
    </Btn>
}