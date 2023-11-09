import React from 'react';
import { FaAward, FaPhone, FaSeedling, FaTractor } from 'react-icons/fa';
import Image from 'next/image';
import feature from "../../assets/img/feature.png";

const Features = () => {
  return (
    <div className="bg-primary-color">
      <div className="container py-5">
        <div className="mx-auto text-center mb-3 pb-2" >
          <h6 className="uppercase">Features</h6>
          <h1 className=" text-font-light">Why Choose Us!!!</h1>
        </div>
        <div className="grid grid-flow-col">
          <div className="col-span-3">
            <div className="text-font-light mb-5">
              <div className="flex items-center justify-center mb-3" >
                <FaSeedling />
              </div>
              <h4 className="text-font-light">100% Organic</h4>
              <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita</p>
            </div>
            <div className="text-font-light">
              <div className="flex items-center justify-center mb-3" >
                <FaAward />
              </div>
              <h4 className="text-font-light">Award Winning</h4>
              <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita</p>
            </div>
          </div>
          <div className="col-lg-6">
            <div className="d-block bg-font-light h-100 text-center p-5 pb-lg-0">
              <p>At et justo elitr amet sea at. Magna et sit vero at ipsum sit et dolores rebum. Magna sea eos sit dolor, ipsum amet no tempor ipsum eirmod lorem eirmod diam tempor dolor eos diam et et diam dolor ea. Clita est rebum amet dolore sit. Dolor stet dolor duo clita, vero dolor ipsum amet dolore magna lorem erat stet sed vero dolor</p>
              <Image className="" src={feature} alt="" />
            </div>
          </div>
          <div className="col-span-3">
            <div className="text-font-light mb-5">
              <div className="flex items-center justify-center mb-3" >
                <FaTractor />
              </div>
              <h4 className="text-font-light">Modern Farming</h4>
              <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita</p>
            </div>
            <div className="text-font-light">
              <div className="flex items-center justify-center mb-3" >
                <FaPhone />
              </div>
              <h4 className="text-font-light">24/7 Support</h4>
              <p className="mb-0">Labore justo vero ipsum sit clita erat lorem magna clita</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Features