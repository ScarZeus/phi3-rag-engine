import { useRef, useState } from "react";
import "./index.css";

export default function InputFeild() {

    const [message,setMessage]=useState("");

    const textareaRef=useRef(null);

    const resize=()=>{

        textareaRef.current.style.height="0px";
        textareaRef.current.style.height=
        textareaRef.current.scrollHeight+"px";

    }

    return(

        <div className="chat-input-wrapper">

            <div className="chat-input">

                <button className="icon-btn">
                    +
                </button>

                <textarea
                    ref={textareaRef}
                    rows={1}
                    value={message}
                    onChange={(e)=>{
                        setMessage(e.target.value);
                        resize();
                    }}
                    placeholder="Message..."
                />

                <button
                    className={`send-btn ${message.trim()?"active":""}`}
                >
                    ↑
                </button>

            </div>

        </div>

    );

}