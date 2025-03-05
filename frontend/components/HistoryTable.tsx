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
    <div>
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead className='px-2 text-light-200'>Timestamp</TableHead>
                    <TableHead className='px-2 text-light-200'>Person Detected</TableHead>
                    <TableHead className='px-2 text-light-200'>Detection Directory</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {records.map((t: Records) => {
                    return(
                        <TableRow 
                            key={t.id}
                            className='text-light-100'
                        >
                            <TableCell className="min-w-32 pl-2 pr-10">
                                {formatDateTime(new Date(t.createdAt)).dateTime}
                            </TableCell>
                            <TableCell className='max-w-[250px] pl-2 pr-10'>
                                <div className='flex items-center justify-center gap-3 w-full'>
                                    <p className='text-14 truncate font-semibold'>
                                        {t.personCount}
                                    </p>
                                </div>
                            </TableCell>
                            <TableCell className='max-w-[250px] pl-2 pr-10'>
                                <div className='flex items-center justify-center gap-3 w-full'>
                                    <p className='text-14 truncate'>
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