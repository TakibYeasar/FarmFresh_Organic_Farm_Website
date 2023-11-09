import React from 'react';
import Image from 'next/image';
import blog01 from "../../assets/img/blog-1.jpg";
import blog02 from "../../assets/img/blog-2.jpg";
import blog03 from "../../assets/img/blog-3.jpg";

const data = [
  {
    image: blog01,
    title: "Lorem elitr magna stet eirmod labore amet",
    date: "Jan 01, 2050",
  },
  {
    image: blog02,
    title: "Lorem elitr magna stet eirmod labore amet",
    date: "Jan 01, 2050",
  },
  {
    image: blog03,
    title: "Lorem elitr magna stet eirmod labore amet",
    date: "Jan 01, 2050",
  },
]

const Blog = () => {
  return (
    <div className="container">
      <div className="mx-auto text-center mb-5" >
        <h6 className="uppercase">Our Blog</h6>
        <h1 className="text-6xl font-bold text-tertiary-color">Latest Articles From Our Blog Post</h1>
      </div>
      <div className="grid grid-flow-col gap-4">

        {data.map((item, i) => (
          <div className="col-span-4 bg-primary-colo" key={i}>
            <div className="relative">
              <Image className="" src={item?.image} alt="" />
              <a className="absolute top-0" href="">
                <h4 className="text-font-light">{item?.title}</h4>
                <span className="text-font-light">{item?.date}</span>
              </a>
            </div>
          </div>
        ))}

      </div>
    </div>
  )
}

export default Blog