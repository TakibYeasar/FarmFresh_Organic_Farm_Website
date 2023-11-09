import React from 'react';
import Image from 'next/image';
import blog01 from "../../assets/img/blog-1.jpg";
import blog02 from "../../assets/img/blog-2.jpg";
import blog03 from "../../assets/img/blog-3.jpg";

const postdata = [
    {
        image: blog01,
    },
    {
        image: blog02,
    },
    {
        image: blog03,
    },
    {
        image: blog01,
    },
    {
        image: blog02,
    },
    {
        image: blog03,
    },
]

const Recentpost = () => {
  return (
      <div className='container'>
          <div className="mb-5">
              <h2 className="mb-4">Recent Post</h2>
              <div className="p-4">
                  
                  {postdata.map((item, i) => (
                      <div className="flex overflow-hidden mb-3">
                          <Image className="" src={item?.image} alt="" />
                          <a href="" className="flex items-center bg-white text-font-color px-3 mb-0">Lorem ipsum dolor sit amet elit
                          </a>
                      </div>
                  ))}

                  
              </div>
          </div>
    </div>
  )
}

export default Recentpost