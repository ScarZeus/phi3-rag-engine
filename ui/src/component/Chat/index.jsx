import { useEffect, useRef, useState } from "react";
import "./index.css";
import InputFeild from "../InputFeild";

export default function Chat() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: "assistant",
      content: "Hello! How can I help you today."
    }
  ]);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [messages]);

  return (
    <div className="chat-container">

      <div className="chat-header">
        <h2>Phi-3 Assistant</h2>
      </div>

      <div className="messages">

        {messages.map(message => (
          <div
            key={message.id}
            className={`message-row ${message.role}`}
          >
            <div className="bubble">
              {message.content}
            </div>
          </div>
        ))}

        <div ref={bottomRef} />

      </div>

      <InputFeild />

    </div>
  );
}