import HistoryTable from '@/components/HistoryTable'
import { fetchRecord } from '@/lib/actions';
import React from 'react'

// Make page dynamic to prevent prerendering at build time
export const dynamic = 'force-dynamic';

const History = async () => {
  let records = [];
  
  try {
    records = await fetchRecord();
    console.log(records);
  } catch (error) {
    console.error('Error fetching records:', error);
    // Continue with empty records array
  }
  
  return (
    <section>
      <div className='flex flex-col items-center'>
        <h2 className='text-2xl font-semibold text-light-200'>Detection History</h2>
      </div>
      <div className='mt-3'>
        <HistoryTable records={records} />
      </div>
    </section>
  )
}

export default History