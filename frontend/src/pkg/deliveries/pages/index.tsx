import React from 'react';
import UploadForm from '../components/upload_form';

const HomePage: React.FC = () => {
  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '2rem' }}>
      <h1>Person Detection App</h1>
      <UploadForm />
    </div>
  );
};

export default HomePage;
