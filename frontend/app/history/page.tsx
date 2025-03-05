"use client";

import { useEffect, useState } from "react";
import { fetchDetectionHistory } from "@/pkg/repositories/show_history";

import { DetectionRecord } from "@/shared/models/detection_record";

export default function HistoryPage() {
  const [records, setRecords] = useState<DetectionRecord[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const history = await fetchDetectionHistory();
        setRecords(history);
      } catch (error) {
        console.error("Error fetching detection history:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  console.log(records)

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h1>Detection History</h1>
      <table border={1} cellPadding={8} style={{ marginTop: "20px", width: "100%" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Time</th>
            <th>Person Count</th>
            <th>Detected Image</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{formatDateTime(record.createdAt)}</td>
              <td>{record.personCount}</td>
              <td>{record.outputSaveDir}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function formatDateTime(timestamp: string | number | Date): string {
  try {
    if (typeof timestamp === 'string' && timestamp.match(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$/)) {
      const parts = timestamp.split('.');
      const datePart = parts[0]; // 2025-03-05T02:01:44
      const microseconds = parts[1] || '000';
      const milliseconds = microseconds.substring(0, 3); // Take only first 3 digits
      
      return new Date(`${datePart}.${milliseconds}Z`).toLocaleString();
    }
    
    return new Date(timestamp).toLocaleString();
  } catch (error) {
    console.error("Error formatting date:", error);
    return 'Invalid date';
  }
}