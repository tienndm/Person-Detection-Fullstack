"use client";
import React, { useState, ChangeEvent, FormEvent } from 'react';
import { detectPersons } from '@/usecases/core';
import { PersonDetectionResult } from '@/shared/models/person_detection_result';

const UploadForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<PersonDetectionResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    setError(null);
    try {
      const res = await detectPersons(file);
      setResult(res);
    } catch (err: any) {
      setError(err.message || 'Error occurred during detection');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Upload Image for Person Detection</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit" disabled={!file || loading}>
          Detect Persons
        </button>
      </form>
      {loading && <p>Processing...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {result && (
        <div>
          <p>{result.message}</p>
          <p>Số người được trong hình: {result.personCount}</p>
          <img
            src={result.image}
            alt="Detection Result"
            style={{ maxWidth: '100%', height: 'auto' }}
          />
        </div>
      )}
    </div>
  );
};

export default UploadForm;
