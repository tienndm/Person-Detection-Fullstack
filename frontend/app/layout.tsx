"use client";

import Link from "next/link";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="container">
          <header>
            <h1>Person Detection App</h1>
            <nav style={{ padding: "10px", background: "#f0f0f0", marginBottom: "20px" }}>
              <Link href="/" style={{ marginRight: "20px" }}>Home</Link>
              <Link href="/history">History</Link>
            </nav>
          </header>
          <main>{children}</main>
          <footer>
            <p>&copy; 2025 Tien Nguyen</p>
          </footer>
        </div>
        <style jsx>{`
          .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
          }
          header, footer {
            background: #0070f3;
            color: white;
            padding: 10px;
          }
        `}</style>
      </body>
    </html>
  );
}
