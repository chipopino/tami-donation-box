import React, { useEffect, useState } from 'react';
import { get } from 'src/fetch';
import { d_giffs } from 'src/methodes/routs';

export default function Giffs() {

    const [gifs, setGifs] = useState<string[]>([]);
    useEffect(() => {
        get('getGifNames')
            //@ts-ignore
            .then(result => setGifs(result))
            .catch(err => console.log(err))
    }, []);

    return <div className='flex flex-col gap-2 w-full p-4'>
        {gifs.map((e: string, i) =>
            <div className='flex flex-col'>
                <span>{e}</span>
                <img
                    className='w-full border'
                    key={`k_${e}_${i}`}
                    src={d_giffs(e)}
                    alt={e}
                />
            </div>
        )}
    </div>
}