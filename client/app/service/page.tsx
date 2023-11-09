import { Service, Testimonial } from '@/containers';
import React from 'react';

const page = () => {
  return (
    <div className='container'>
          <div className="grid justify-start">
            <div className="col-span-8 text-center">
              <h1 className=" text-font-light">Our Services</h1>
              <a href="" className="me-3">Home</a>
              <a href="" className="">Services</a>
            </div>
          </div>

      <Service />
      
      <Testimonial />
    </div>
  )
}

export default page