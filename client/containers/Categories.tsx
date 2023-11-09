import React from 'react'
import { FaArrowRight } from 'react-icons/fa'

const Categories = () => {
  return (
      <div className='categories'>
          <div className="mb-5">
              <h2 className="mb-4">Categories</h2>
              <div className="flex justify-start p-4">
                  <a className=" text-font-light mb-2" href="#"><FaArrowRight />Web Design</a>
                  <a className=" text-font-light mb-2" href="#"><FaArrowRight />Web Development</a>
                  <a className=" text-font-light mb-2" href="#"><FaArrowRight />Web Development</a>
                  <a className=" text-font-light mb-2" href="#"><FaArrowRight />Keyword Research</a>
                  <a className=" text-font-light" href="#"><FaArrowRight />Email Marketing</a>
              </div>
          </div>
    </div>
  )
}

export default Categories