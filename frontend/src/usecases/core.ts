import { uploadImageForDetection } from '@/pkg/repositories/person_detection';
import { PersonDetectionResult } from '@/shared/models/person_detection_result';

export async function detectPersons(file: File): Promise<PersonDetectionResult> {
  return uploadImageForDetection(file);
}
