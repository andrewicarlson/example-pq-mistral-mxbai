import React from 'react';

const ActionProvider = ({ createChatBotMessage, setState, children }) => { 
    const handleMessage = async (message) => {    
        const response = await fetch(`http://0.0.0.0:8000?question=${message}`, {
            method: "GET",
            mode: "cors"
        });

        const llmResponse = await response.json();

        const botMessage = createChatBotMessage(llmResponse);
    
        setState((prev) => ({      
            ...prev,      
            messages: [...prev.messages, botMessage],    
        }));  
    };

    return (
        <div>      
            {React.Children.map(children, (child) => {
                return React.cloneElement(child, { actions: {
                    handleMessage
                }, }); 
            })}    
        </div>
    ); 
};

export default ActionProvider;