import { formatDateTime } from '@/lib/utils'
import { 
    Table, 
    TableBody, 
    TableCell, 
    TableHead, 
    TableHeader, 
    TableRow
} from './ui/table'
import React from 'react'
import { HistoryTableProps, Records } from '@/types'


const HistoryTable = ({records}: HistoryTableProps) => {
  return (
    <div className="w-full overflow-x-auto">
        <Table className="min-w-full">
            <TableHeader>
                <TableRow>
                    <TableHead className="px-2 text-light-200 whitespace-nowrap text-center">ID</TableHead>
                    <TableHead className="px-2 text-light-200 whitespace-nowrap text-center">Timestamp</TableHead>
                    <TableHead className="px-2 text-light-200 whitespace-nowrap text-center">Person Detected</TableHead>
                    <TableHead className="px-2 text-light-200 whitespace-nowrap text-center">Detection Directory</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {records.map((t: Records) => {
                    return(
                        <TableRow 
                            key={t.id}
                            className="text-light-100"
                        >
                            <TableCell>
                                <div className="flex items-center justify-center gap-3">
                                    <p className="text-14 font-semibold text-center">
                                        {t.id}
                                    </p>
                                </div>
                            </TableCell>
                            <TableCell className="whitespace-nowrap pl-2 pr-10">
                                {formatDateTime(new Date(t.createdAt)).dateTime}
                            </TableCell>
                            <TableCell className="pl-2 pr-10 text-center">
                                <div className="flex items-center justify-center gap-3">
                                    <p className="text-14 font-semibold text-center">
                                        {t.personCount}
                                    </p>
                                </div>
                            </TableCell>
                            <TableCell className="pl-2 pr-10 break-words">
                                <div className="flex items-center gap-3">
                                    <p className="text-14 break-all">
                                        {t.outputSaveDir}
                                    </p>
                                </div>
                            </TableCell>
                        </TableRow>
                    )
                })}
            </TableBody>
        </Table>
    </div>
  )
}

export default HistoryTable