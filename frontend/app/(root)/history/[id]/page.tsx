import HistoryTable from '@/components/HistoryTable'
import HistroyPagination from '@/components/HistoryPagination';
import { fetchRecord, fetchTotalPage } from '@/lib/actions';
import React from 'react'

const History = async ({params}: {params: Promise<{id: number}> }) => {
  const currentPage = (await params).id
  const records = await fetchRecord(currentPage)
  const totalPages = await fetchTotalPage()
  return (
    <section>
      <div className='flex flex-col items-center'>
        <h2 className='text-2xl font-semibold text-light-200'>Detection History</h2>
      </div>
      <div className='mt-3'>
        <HistoryTable records={records} />
      </div>
      <div className='mt-3'>
        <HistroyPagination currentPage={currentPage} totalPages={totalPages}/>
      </div>
    </section>
  )
}

export default History