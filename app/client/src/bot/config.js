import { createChatBotMessage } from 'react-chatbot-kit';

const config = {  
    initialMessages: [createChatBotMessage(`Hi, you can ask me questions about what we sell or the price of a product like papayas.`)],
    botName: "Sojourner",
    customStyles: {  
        chatButton: {      
            backgroundColor: '#fc5200',    
        },  
    },
};
export default config;