import React from 'react';
import Image from 'next/image';
import about from "../../assets/img/about.png";
import { FaAward, FaCheck, FaMugHot, FaSlideshare, FaStar, FaUser } from 'react-icons/fa';

const About = () => {
  return (
    <>
      <div className="container">
        <div className="grid grid-flow-col">
          <div className="col-span-6 mb-5">
            <div className="flex h-100 pt-4 border border-primary-color">
              <Image className="mt-auto mx-auto" src={about} alt='' />
            </div>
          </div>
          <div className="col-span-6 pb-5">
            <div className="mb-3 pb-2">
              <h6 className="uppercase text-xl font-semibold text-primary-color">About Us</h6>
              <h1 className="text-4xl font-bold text-tertiary-color">We Produce Organic Food For Your Family</h1>
            </div>
            <p className="mb-4">Tempor erat elitr at rebum at at clita. Diam dolor diam ipsum et tempor sit. Clita erat ipsum et lorem et sit, sed stet no labore lorem sit. Sanctus clita duo justo et tempor eirmod magna dolore erat amet magna</p>
            <div className="grid grid-flow-col">
              <div className="col-span-6 flex p-4">
                <FaSlideshare className="text-xl text-tertiary-color mr-4" />
                <h4>100% Organic</h4>
                <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero</p>
              </div>
              <div className="col-span-6 flex p-4">
                <FaAward className="text-xl text-tertiary-color mr-4" />
                <h4>Award Winning</h4>
                <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-primary-color">
        <div className="container grid grid-flow-col">
          <div className="col-span-3 col-md-6">
            <div className="flex">
              <div className="rounded flex items-center justify-center mb-3" >
                <FaStar />
              </div>
              <div className="ps-4">
                <h5 className="text-white">Our Experience</h5>
                <h1 className="text-white mb-0">12345</h1>
              </div>
            </div>
          </div>
          <div className="col-span-3 col-md-6">
            <div className="flex">
              <div className="rounded flex items-center justify-center mb-3" >
                <FaUser />
              </div>
              <div className="ps-4">
                <h5 className="text-white">Farm Specialist</h5>
                <h1 className="text-white mb-0">12345</h1>
              </div>
            </div>
          </div>
          <div className="col-span-3 col-md-6">
            <div className="flex">
              <div className="rounded flex items-center justify-center mb-3" >
                <FaCheck />
              </div>
              <div className="ps-4">
                <h5 className="text-white">Complete Project</h5>
                <h1 className="text-white mb-0">12345</h1>
              </div>
            </div>
          </div>
          <div className="col-span-3 col-md-6">
            <div className="flex">
              <div className="rounded flex items-center justify-center mb-3" >
                <FaMugHot />
              </div>
              <div className="ps-4">
                <h5 className="text-white">Happy Clients</h5>
                <h1 className="text-white mb-0">12345</h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default About