import { useRef, useState } from "react";
import "./index.css";

export default function InputFeild() {
  const [message, setMessage] = useState("");
  const textareaRef = useRef(null);

  const resize = () => {
    textareaRef.current.style.height = "0px";
    textareaRef.current.style.height =
      textareaRef.current.scrollHeight + "px";
  };

  const send = () => {
    if (!message.trim()) return;

    console.log(message);

    setMessage("");
    textareaRef.current.style.height = "52px";
  };

  return (
    <div className="chat-input-wrapper">
      <div className="chat-input">

        <button className="icon-btn">
          📎
        </button>

        <textarea
          ref={textareaRef}
          rows={1}
          placeholder="Ask anything..."
          value={message}
          onChange={(e) => {
            setMessage(e.target.value);
            resize();
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              send();
            }
          }}
        />

        <button
          className={`send-btn ${message.trim() ? "active" : ""}`}
          onClick={send}
        >
          ↑
        </button>

      </div>
    </div>
  );
}