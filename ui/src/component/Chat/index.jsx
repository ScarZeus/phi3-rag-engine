import { useEffect, useRef, useState } from "react";
import "./index.css";
import InputFeild from "../InputFeild";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Phi-3 Assistant</h2>
      </div>

      <div className="messages">
        {messages.length === 0 ? (
          <div className="empty-chat">
            <div className="bubble assistant">
              👋 Hi! I'm happy to help you. Ask me anything to get started.
            </div>
          </div>
        ) : (
          messages.map((message) => (
            <div
              key={message.id}
              className={`message-row ${message.role}`}
            >
              <div className="bubble">
                {message.content}
              </div>
            </div>
          ))
        )}

        <div ref={bottomRef} />
      </div>

      <InputFeild />
    </div>
  );
}