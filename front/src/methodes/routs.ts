import urlJoin from 'url-join';

export const d_root = (...args: string[]) =>{
    return urlJoin(process.env.URL_BACK || '', ...args); 
}
export const d_fileUpload = (...args: string[]) =>{
    return d_root('upload', ...args); 
}
export const d_giffs = (...args: string[]) =>{
    return d_root('gifs', ...args); 
}