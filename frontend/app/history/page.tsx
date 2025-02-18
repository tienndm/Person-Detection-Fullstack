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
            <th>Input Image</th>
            <th>Detected Image</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{new Date(record.timestamp).toLocaleString()}</td>
              <td>{record.person_count}</td>
              <td>{record.input_save_dir}</td>
              <td>{record.output_save_dir}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}