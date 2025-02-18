import { DetectionRecord } from "@/shared/models/detection_record";

export async function fetchDetectionHistory(): Promise<DetectionRecord[]> {
  const response = await fetch("http://localhost:8632/api/v1/fetch");

  if (!response.ok) {
    throw new Error("Failed to fetch detection history");
  }

  const data = await response.json();
  return data.data;
}