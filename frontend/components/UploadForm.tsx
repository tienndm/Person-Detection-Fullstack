"use client"
import React, { ChangeEvent, FormEvent, useState } from 'react'
import { Button } from './ui/button'
import { detectPerson } from '@/lib/actions'
import { PersonDetectionResult } from '@/types'
import Image from 'next/image'

const UploadForm = () => {
  const [file, setFile] = useState<File | null>(null)
  const [result, setResult] = useState<PersonDetectionResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
    }
  }

  const handleSubmit = async(e: FormEvent) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    setError(null);
    try {
      const res = await detectPerson(file);
      setResult(res)
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch(error: any) {
      setError(error.message || 'Error occurred during detection')
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className='flex flex-wrap gap-2'>
        <h2 className='text-xl font-semibold text-light-200 items-center'>
            Upload Image for Person Detection
        </h2>
        <form onSubmit={handleSubmit} className='flex flex-col items-center gap-4 mt-6 w-full max-w-md mx-auto'>
          <input 
            type='file' 
            accept='image/*' 
            onChange={handleFileChange}
            className="w-full border border-gray-300 rounded p-2 text-light-200"
            disabled={loading}
          />
          <Button type='submit' disabled={!file || loading} className="w-full">
            {loading ? 'Processing...' : 'Count People'}
          </Button>
          
          {error && <p className="text-red-500 mt-2">{error}</p>}
          
          {result && (
            <div className="mt-4 w-full flex flex-col items-center text-center">
              <h3 className="text-lg font-medium text-light-400">Detection Results</h3>
              <p className='text-light-200'>Person detected: {result.personCount}</p>
              <Image 
                src={result.image} 
                alt='detection-res' 
                width={400}
                height={300}
                className='mt-5'
              />
            </div>
          )}
        </form>
    </div>
  )
}

export default UploadForm