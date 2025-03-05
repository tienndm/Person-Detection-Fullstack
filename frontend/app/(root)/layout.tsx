import Footer from '@/components/Footer'
import Header from '@/components/Header'
import React, { ReactNode } from 'react'

const Layout = async ({ children }: { children: ReactNode }) => {
  return <main className='root-container'>
    <div className='mx-auto max-w-7xl'>
      <Header />
      <div className='mt-20 pb-20'>
        {children}
      </div>
      <Footer />
    </div>
  </main>
}

export default Layout