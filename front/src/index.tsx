import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { get, post } from 'src/fetch';
import Button from '@mui/material/Button';
import './index.css';

const App: React.FC = () => {
  useEffect(() => {
    get('/')
      .then(res => console.log(res))
    post('/test', { test: 'test' })
      .then(res => console.log(res))
  }, [])
  return <>
    <div className='p-8'>Hello, world!</div>
    <Button variant="contained" color="primary">
      MUI Button
    </Button>
  </>
};

//@ts-ignore
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<App />);