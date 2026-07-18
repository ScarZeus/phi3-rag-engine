import { useRef, useState } from "react";
import "./index.css";
import useUploads from "../hooks/useUploads";

export default function Drawer({ sessionId }) {
  const [files, setFiles] = useState([]);

  const inputRef = useRef(null);

  const {
    uploading,
    uploadedFiles,
    error,
    uploadFiles,
  } = useUploads();

  const handleFiles = (e) => {
    setFiles((prev) => [
      ...prev,
      ...Array.from(e.target.files),
    ]);

    // Allow selecting the same file again later
    e.target.value = "";
  };

  const handleUpload = async () => {
    if (files.length === 0) return;

    try {
      await uploadFiles(sessionId, files);
      setFiles([]); // Clear selected files after successful upload
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <aside className="sidebar">
      <h2>Uploaded Files</h2>

      <p className="subtitle">
        Upload and manage your documents.
      </p>

      <div
        className="upload-box"
        onClick={() => inputRef.current.click()}
      >
        <div className="upload-icon">☁️</div>

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
        {files.length === 0 ? (
          <p>No files selected.</p>
        ) : (
          files.map((file, index) => (
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
                  {(file.size / 1024).toFixed(1)} KB
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {uploadedFiles.length > 0 && (
        <div className="uploaded-list">
          <h4>Uploaded</h4>

          {uploadedFiles.map((name) => (
            <div key={name}>{name}</div>
          ))}
        </div>
      )}

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      <button
        className="upload-btn"
        onClick={handleUpload}
        disabled={uploading || files.length === 0}
      >
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </aside>
  );
}