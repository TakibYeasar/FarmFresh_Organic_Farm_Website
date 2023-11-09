import React from 'react';
import Image from 'next/image';
import blog01 from "../../../assets/img/blog-1.jpg";
import blog02 from "../../../assets/img/blog-2.jpg";
import blog03 from "../../../assets/img/blog-3.jpg";
import { FaArrowRight, FaArrowLeft, FaSearch } from "react-icons/fa";
import { Blogtags, Categories, Recentpost } from '@/containers';


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

const page = () => {
  return (
    <div className="container">
      <div className="grid justify-start">
        <div className="col-span-8 text-center">
          <h1 className=" text-font-light">Blog Grid</h1>
          <a href="" className="me-3">Home</a>
          <a href="" className="">Blog Grid</a>
        </div>
      </div>

      <div className="grid">
        <div className="col-span-8">
          <div className="grid">

            {data.map((item, i) => (
              <div className="col-span-6">
                <div className="relative overflow-hidden" key={i}>
                  <Image className="" src={item?.image} alt="" />
                  <a className="" href="">
                    <h4 className="text-font-light">{item?.title}</h4>
                    <span className="text-font-light">{item?.date}</span>
                  </a>
                </div>
              </div>
            ))}


            <div className="col-span-12">
              <nav aria-label="">
                <ul className="justify-center m-0">
                  <li className="">
                    <a className="" href="#"><span aria-hidden="true"><FaArrowLeft /></span></a>
                  </li>
                  <li className=""><a className="" href="#">1</a></li>
                  <li className=""><a className="" href="#">2</a></li>
                  <li className=""><a className="" href="#">3</a></li>
                  <li className="">
                    <a className="" href="#"><span aria-hidden="true"><FaArrowRight /></span></a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>

        <div className="col-span-4">
          <div className="mb-5">
            <div className="">
              <input type="text" className="p-3" placeholder="Keyword" />
              <button className="px-4"><FaSearch /></button>
            </div>
          </div>

          <Categories />

          <Recentpost />

          <div className="mb-5">
            <Image src={blog01} alt="" className="rounded" />
          </div>

          <Blogtags />

          <div>
            <h2 className="mb-4">Plain Text</h2>
            <div className="text-center text-font-light" >
              <p>Vero sea et accusam justo dolor accusam lorem consetetur, dolores sit amet sit dolor clita kasd justo, diam accusam no sea ut tempor magna takimata, amet sit et diam dolor ipsum amet diam</p>
              <a href="" className="btn-style">Read More</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default page