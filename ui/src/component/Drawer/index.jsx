import { useRef, useState } from "react";
import "./index.css";

export default function Drawer() {

    const [files,setFiles]=useState([]);

    const inputRef=useRef(null);

    const handleFiles=(e)=>{

        setFiles(prev=>[
            ...prev,
            ...Array.from(e.target.files)
        ]);

    }

    return(

        <aside className="sidebar">

            <h2>Uploaded Files</h2>

            <p className="subtitle">
                Upload and manage your documents.
            </p>

            <div
                className="upload-box"
                onClick={()=>inputRef.current.click()}
            >

                <div className="upload-icon">
                    ☁️
                </div>

                <h3>Select Files</h3>

                <p>PDF, DOCX, TXT</p>

                <input
                    hidden
                    ref={inputRef}
                    type="file"
                    multiple
                    onChange={handleFiles}
                />

            </div>

            <div className="file-list">

                {

                    files.length===0 ?

                    <p>No files uploaded.</p>

                    :

                    files.map((file,index)=>(

                        <div
                            key={index}
                            className="file-card"
                        >

                            <span>📄</span>

                            <div>

                                <div className="name">
                                    {file.name}
                                </div>

                                <div className="size">
                                    {(file.size/1024).toFixed(1)} KB
                                </div>

                            </div>

                        </div>

                    ))

                }

            </div>

            <button className="upload-btn">
                Upload
            </button>

        </aside>

    );

}