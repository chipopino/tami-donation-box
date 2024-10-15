import React, { useEffect, useState } from 'react';
import { get } from 'src/fetch';
import { d_giffs } from 'src/methodes/routs';
import { urlify } from 'src/methodes/functions';
import CloseIcon from '@mui/icons-material/Close';

export default function Giffs() {

    const [gifs, setGifs] = useState<string[]>([]);
    useEffect(() => {
        get('getGifNames')
            //@ts-ignore
            .then(result => setGifs(result))
            .catch(err => console.log(err))
    }, []);

    return <div className='flex flex-col gap-2 w-full p-4 items-center justify-center'>
        {gifs.map((gif: string, i) =>
            <div
                key={`k_${gif}_${i}`}
                className='w-full max-w-[400px] flex flex-col items-center justify-center'
            >
                <span>{gif}</span>
                <div className='flex gap-2 w-full items-center justify-center'>
                    <img
                        className='w-full border'
                        src={d_giffs(gif)}
                        alt={gif}
                    />
                    <CloseIcon
                        className='cursor-pointer'
                        onClick={() => {
                            if (confirm(`are you sure you whant to delete "${gif}"`)) {
                                get(`/deleteGif/${urlify(gif)}`)
                                    .then(() => {
                                        window.alert(`"${gif}" deleted successfully`);
                                        setGifs(old => old.filter(e => e !== gif));
                                    })
                                    .catch(() => window.alert(`could not delete ${gif}`))
                            }
                        }}
                    />
                </div>
            </div>
        )}
    </div>
}