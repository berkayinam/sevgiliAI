import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input;
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      const response = await axios.post('http://localhost:2300/chat', {
        message: userMessage
      });

      setMessages(prev => [...prev, { role: 'assistant', content: response.data.response }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Üzgünüm, bir hata oluştu. Lütfen tekrar dene.' }]);
    }

    setIsLoading(false);
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      {/* Header with Berkay's photo */}
      <div className="bg-white p-4 shadow-md flex items-center space-x-4">
        <img 
          src="/berkay.jpeg" 
          alt="Berkay" 
          className="w-12 h-12 rounded-full object-cover border-2 border-blue-500"
        />
        <div>
          <h1 className="text-xl font-bold text-gray-800">Berkay AI</h1>
          <p className="text-sm text-gray-600">Sevgili Asistanı</p>
        </div>
      </div>

      {/* Chat messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            {message.role === 'assistant' && (
              <img 
                src="/berkay.jpeg" 
                alt="Berkay" 
                className="w-8 h-8 rounded-full object-cover mr-2"
              />
            )}
            <div
              className={`max-w-[70%] rounded-lg p-3 ${
                message.role === 'user'
                  ? 'bg-blue-500 text-white'
                  : 'bg-white text-gray-800'
              }`}
            >
              {message.content}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <img 
              src="/berkay.jpeg" 
              alt="Berkay" 
              className="w-8 h-8 rounded-full object-cover mr-2"
            />
            <div className="bg-white text-gray-800 rounded-lg p-3">
              Yazıyor...
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input form */}
      <form onSubmit={handleSubmit} className="p-4 border-t bg-white">
        <div className="flex space-x-4">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Mesajınızı yazın..."
            className="flex-1 p-2 border rounded-lg focus:outline-none focus:border-blue-500"
          />
          <button
            type="submit"
            disabled={isLoading}
            className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 focus:outline-none disabled:opacity-50"
          >
            Gönder
          </button>
        </div>
      </form>
    </div>
  );
}

export default App; 