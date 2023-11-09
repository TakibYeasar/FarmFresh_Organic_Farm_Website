import React from 'react';
import { FaFacebook, FaTwitter, FaLinkedinIn, FaInstagram } from "react-icons/fa";
import Image from 'next/image';
import team01 from "../../assets/img/team-1.jpg";
import team02 from "../../assets/img/team-2.jpg";
import team03 from "../../assets/img/team-3.jpg";

const data = [
  {
    image: team01,
    title: "Farmer Name",
    dest: ">Designation",
  },
  {
    image: team02,
    title: "Farmer Name",
    dest: ">Designation",
  },
  {
    image: team03,
    title: "Farmer Name",
    dest: ">Designation",
  },
]

const Team = () => {
  return (
    <div className="container">
      <div className="mx-auto text-center mb-5" >
        <h6 className="text-primary text-uppercase">The Team</h6>
        <h1 className="display-5">We Are Professional Organic Farmers</h1>
      </div>
      <div className="grid grid-flow-col gap-4">

        {data.map((item, i) => (
          <div className="col-span-4" key={i}>
            <div className="grid grid-flow-col">
              <div className="col-span-10">
                <div className="relative">
                  <Image className="w-100" src={item?.image} alt="" />
                  <div className="absolute start-0 bottom-0 w-100 py-3 px-4" >
                    <h4 className="text-font-light">{item?.title}</h4>
                    <span className="text-font-light">{item?.dest}</span>
                  </div>
                </div>
              </div>
                <div className="col-span-2 h-100 grid items-center justify-around py-5">
                  <a className="rounded bg-bg-color" href="#"><FaTwitter /></a>
                  <a className="rounded bg-bg-color" href="#"><FaFacebook /></a>
                  <a className="rounded bg-bg-color" href="#"><FaLinkedinIn /></a>
                  <a className="rounded bg-bg-color" href="#"><FaInstagram /></a>
                </div>
            </div>
          </div>
        ))}

      </div>
    </div>
  )
}

export default Team