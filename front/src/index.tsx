import React from 'react';
import ReactDOM from 'react-dom/client';
import Title from 'components/Title';
import ToggleLeds from 'components/ToggleLeds';
import SubmitGiff from 'components/SubmitGiff';
import Giffs from 'components/Giffs';
import 'src/index.css';

const App: React.FC = () => {

  return <div className="w-full h-full flex flex-col items-center justify-center gap-4 p-8">
    <Title />
    <ToggleLeds />
    <SubmitGiff />
    <Giffs />
  </div>
};

//@ts-ignore
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<App />);