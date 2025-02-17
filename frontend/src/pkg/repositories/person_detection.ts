import { PersonDetectionResult } from '@/shared/models/person_detection_result';

export async function uploadImageForDetection(file: File): Promise<PersonDetectionResult> {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('http://localhost:8632/detect-persons/', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Failed to upload image');
  }
  return response.json();
}
