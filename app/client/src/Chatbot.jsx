import Chatbot from 'react-chatbot-kit';
import 'react-chatbot-kit/build/main.css';

import config from './bot/config.js';
import MessageParser from './bot/MessageParser.jsx';
import ActionProvider from './bot/ActionProvider.jsx';

export const ChatbotComponent = () => { 
    return (
        <div>      
            <Chatbot config={config} messageParser={MessageParser} actionProvider={ActionProvider} />    
        </div>
    ); 
};