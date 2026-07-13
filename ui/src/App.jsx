import "./App.css";
import Drawer from "./component/Drawer";
import Chat from "./component/Chat";

export default function App() {
  return (
    <div className="layout">
      <Drawer />

      <main className="content">
        <Chat />
      </main>
    </div>
  );
}