import { useState } from "react";

export default function useUploads() {
  const [uploading, setUploading] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [error, setError] = useState(null);

  const uploadFiles = async (sessionId, files) => {
    if (!files || files.length === 0) return;

    setUploading(true);
    setError(null);

    try {
      const formData = new FormData();

      Array.from(files).forEach((file) => {
        formData.append("files", file);
      });

      const response = await fetch(
        `http://localhost:8000/upload/${sessionId}`,
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Failed to upload files");
      }

      const data = await response.json();

      setUploadedFiles((prev) => [...prev, ...data.uploaded]);

      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setUploading(false);
    }
  };

  return {
    uploading,
    uploadedFiles,
    error,
    uploadFiles,
  };
}