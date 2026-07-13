import "./App.css";
import Drawer from "./component/Drawer";
import Chat from "./component/Chat";
import { useEffect, useState } from "react";

export default function App() {
  const [session, set_session_id] = useState("")

  useEffect(() => {
    const createSession = async () => {
      try {
        const response = await fetch("http://localhost:8000/session", {
          method: "POST",
        });

        const data = await response.json();

        set_session_id(data.session_id);
      } catch (err) {
        console.error(err);
      }
    };

    createSession();
  }, []);
  return (
    <div className="layout">
      <Drawer />
      <main className="content">
        <Chat />
      </main>
    </div>
  );
}