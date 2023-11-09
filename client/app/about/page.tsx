import React from 'react';
import { About, Team } from '@/containers';

const page = () => {
  return (
    <div>
        <div className="container">
          <div className="grid justify-start">
            <div className="col-span-8 text-center">
              <h1 className=" text-font-light">About Us</h1>
              <a href="" className="me-3">Home</a>
              <a href="" className="">About Us</a>
            </div>
          </div>
        </div>

      <About />
      <Team />
    </div>
  )
}

export default page