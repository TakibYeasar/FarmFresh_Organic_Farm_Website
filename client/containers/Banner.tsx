import React from 'react';
import Image from 'next/image';
import carousel01 from "../../assets/img/carousel-1.jpg";
import carousel02 from "../../assets/img/carousel-2.jpg";
import bgprod01 from "../../assets/img/bg-product-1.png";
import bgprod02 from "../../assets/img/bg-product-2.png";
import { FaArrowRight } from 'react-icons/fa';

const Banner = () => {
  return (
    <div className=''>
      <div className="">
        <div className="relative">
          <Image className="w-screen h-screen" src={carousel01} alt="Image" />
          <div className="absolute top-0 left-0">
            <h3 className="text-font-light">Organic Vegetables</h3>
            <h1 className="text-font-light">Organic Vegetables For Healthy Life</h1>
            <a href="" className="btn-primary">Explore</a>
            <a href="" className="btn-secondary">Contact</a>
          </div>
        </div>
        {/* <div className="">
            <Image className="w-screen h-screen" src={carousel02} alt="Image" />
            <div className="top-0 bottom-0 start-0 end-0 flex justify-center items-center">
              <div className="text-start p-5" >
                <h3 className="text-font-light">Organic Fruits</h3>
                <h1 className="text-font-light">Organic Fruits For Better Health</h1>
                <a href="" className="me-3 btn-primary">Explore</a>
                <a href="" className="btn-secondary">Contact</a>
              </div>
            </div>
          </div> */}
        <button className="" type="button">
          <span className="" aria-hidden="true"></span>
          <span className="hidden">Previous</span>
        </button>
        <button className="" type="button" >
          <span className="" aria-hidden="true"></span>
          <span className="hidden">Next</span>
        </button>
      </div>

      <div className="container">
        <div className="grid grid-flow-col">
          <div className="col-span-6 grid justify-center bg-primary-color p-5" >
            <Image className="" src={bgprod01} alt="Image" />
            <div className="">
              <h3 className="text-font-light mb-3">Organic Vegetables</h3>
              <p className="text-font-light">Dolor magna ipsum elitr sea erat elitr amet ipsum stet justo dolor, amet lorem diam no duo sed dolore amet diam</p>
              <a className="text-font-light flex items-center" href="">Read More<FaArrowRight /></a>
            </div>
          </div>
          <div className="col-span-6 grid justify-center bg-tertiary-color p-5" >
            <Image className="" src={bgprod02} alt="Image" />
            <div className="">
              <h3 className="text-font-light mb-3">Organic Fruits</h3>
              <p className="text-font-light">Dolor magna ipsum elitr sea erat elitr amet ipsum stet justo dolor, amet lorem diam no duo sed dolore amet diam</p>
              <a className="text-font-light flex items-center" href="">Read More<FaArrowRight /></a>
           </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Banner