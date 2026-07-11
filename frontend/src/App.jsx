import { useState } from "react";
import "./App.css";
import Drawer from "./component/Drawer";
import InputFeild from "./component/InputFeild";

function App() {
  const [open, setOpen] = useState(true);

  return (
    <div className="layout">
      <Drawer />

      <main className="content">
          <InputFeild />
      </main>
    </div>
  );
}

export default App;