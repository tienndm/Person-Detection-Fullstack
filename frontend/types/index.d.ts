declare interface Records {
    id: number
    createdAt: string
    personCount: number
    outputSaveDir: string
}

declare interface HistoryTableProps {
    records: Record[];
}

export interface PersonDetectionResult{
    personCount: number;
    message: string;
    image: string;
}

export type UploadFile = File;
