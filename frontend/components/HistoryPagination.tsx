"use client"
import {
    Pagination,
    PaginationContent,
    PaginationEllipsis,
    PaginationItem,
    PaginationLink,
    PaginationNext,
    PaginationPrevious,
  } from "@/components/ui/pagination"
  
import React from 'react'
import { useRouter } from 'next/navigation'

interface HistoryPaginationProps{
  currentPage: number
  totalPages: number
  onPageChange?: (page: number) => void
}

const HistoryPagination = ({currentPage, totalPages, onPageChange}: HistoryPaginationProps) => {
  const router = useRouter()
  
  // Ensure currentPage is a number
  const pageNum = Number(currentPage)

  const navigateToPage = (page: number) => {
    if (page >= 1 && page <= totalPages) {
      // Force the page to be a number
      router.push(`/history/${Number(page)}`)
      
      if (onPageChange) {
        onPageChange(page)
      }
    }
  }

  const renderPageNumbers = () => {
    const pages = []
    const maxPagesToShow = 3
    
    let startPage = Math.max(1, pageNum - Math.floor(maxPagesToShow / 2))
    const endPage = Math.min(totalPages, startPage + maxPagesToShow - 1)
    
    if (endPage - startPage + 1 < maxPagesToShow) {
      startPage = Math.max(1, endPage - maxPagesToShow + 1)
    }

    // First page
    if (startPage > 1) {
      pages.push(
        <PaginationItem key="1">
          <PaginationLink 
            href={`/history/1`}
            onClick={(e) => {
              e.preventDefault()
              navigateToPage(1)
            }}
          >
            1
          </PaginationLink>
        </PaginationItem>
      )

      if (startPage > 2) {
        pages.push(
          <PaginationItem key="start-ellipsis">
            <PaginationEllipsis />
          </PaginationItem>
        )
      }
    }

    for (let i = startPage; i <= endPage; i++) {
      pages.push(
        <PaginationItem key={i}>
          <PaginationLink 
            href={`/history/${i}`}
            isActive={i === pageNum}
            onClick={(e) => {
              e.preventDefault()
              navigateToPage(i)
            }}
          >
            {i}
          </PaginationLink>
        </PaginationItem>
      )
    }

    // Last page
    if (endPage < totalPages) {
      if (endPage < totalPages - 1) {
        pages.push(
          <PaginationItem key="end-ellipsis">
            <PaginationEllipsis />
          </PaginationItem>
        )
      }
      
      pages.push(
        <PaginationItem key={totalPages}>
          <PaginationLink 
            href={`/history/${totalPages}`} 
            onClick={(e) => {
              e.preventDefault()
              navigateToPage(totalPages)
            }}
          >
            {totalPages}
          </PaginationLink>
        </PaginationItem>
      )
    }

    return pages
  }

  return (
    <div className="text-light-200 items-center justify-between">
      <Pagination>
        <PaginationContent>
          <PaginationItem>
            <PaginationPrevious 
              href={pageNum > 1 ? `/history/${pageNum - 1}` : "#"} 
              onClick={(e) => {
                e.preventDefault()
                if (pageNum > 1) {
                  navigateToPage(pageNum - 1)
                }
              }}
              className={pageNum <= 1 ? "pointer-events-none opacity-50" : ""}
            />
          </PaginationItem>
          
          {renderPageNumbers()}
          
          <PaginationItem>
            <PaginationNext 
              href={pageNum < totalPages ? `/history/${Number(pageNum) + 1}` : "#"} 
              onClick={(e) => {
                e.preventDefault()
                if (pageNum < totalPages) {
                  navigateToPage(Number(pageNum) + 1)
                }
              }}
              className={pageNum >= totalPages ? "pointer-events-none opacity-50" : ""}
            />
          </PaginationItem>
        </PaginationContent>
      </Pagination>
    </div>
  )
}

export default HistoryPagination