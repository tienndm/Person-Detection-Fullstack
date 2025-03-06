'use client'

import Image from 'next/image'
import Link from 'next/link'
import React from 'react'
import { Button } from './ui/button'
import { usePathname } from 'next/navigation'

const Header = () => {
  return (
    <header className='my-10 flex justify-between gap-5'>
        <Link href='/'>
            <Image src='/icons/logo.svg' alt='logo' width={40} height={40}/>
        </Link>
        <div>
            <p className='font-semibold text-light-600 font-ibm-plex-sans'>
                Person Detection App
            </p>
            <p className='text-light-100 font-bebas-neue'>
                Version: 1.0.0
            </p>
        </div>
        <ul className='flex flex-row items-center gap-8'>
            <li>
                {usePathname() === '/' ? (
                    <Link href='/history/1'>
                        <Button>History</Button>
                    </Link>
                ) : (
                    <Link href='/'>
                        <Button>Home</Button>
                    </Link>
                )}
            </li>
        </ul>
    </header>
  )
}

export default Header