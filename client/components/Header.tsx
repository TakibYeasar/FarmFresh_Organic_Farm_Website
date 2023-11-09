import React from 'react';
import { FaTwitter, FaFacebook, FaInstagram, FaLinkedinIn, FaPhoneVolume } from "react-icons/fa";

const Header = () => {
  return (
    <>
      <div className="container">
        <div className="px-5 block">
          <div className="grid grid-flow-col items-center py-3">
            <div className="col-span-3 flex items-center justify-start">
              <FaPhoneVolume className="mr-2 text-3xl font-semibold text-primary-color" />
              <h2 className="mb-0 text-3xl font-semibold">+012 345 6789</h2>
            </div>
            <div className="col-span-6 flex items-center justify-center">
              <a href="/" className="">
                <h1 className="m-0 text-4xl font-semibold text-primary-color"><span className="text-secondary-color">Farm</span>Fresh</h1>
              </a>
            </div>
            <div className="col-span-3 flex items-center justify-end">
              <a className='mr-2 ml-2' href="#"><FaTwitter className="text-4xl font-semibold bg-primary-color text-secondary-color p-2 rounded-full" /></a>
              <a className='mr-2 ml-2' href="#"><FaFacebook className="text-4xl font-semibold bg-primary-color text-secondary-color p-2 rounded-full" /></a>
              <a className='mr-2 ml-2' href="#"><FaLinkedinIn className="text-4xl font-semibold bg-primary-color text-secondary-color p-2 rounded-full" /></a>
              <a className='mr-2 ml-2' href="#"><FaInstagram className="text-4xl font-semibold bg-primary-color text-secondary-color p-2 rounded-full" /></a>
            </div>
          </div>
        </div>
      </div>


      <nav className="bg-primary-color">
        <div className="container flex">
          <div className="mx-auto py-0 flex pt-6 pb-6">
            <a href="/" className="nav-link uppercase font-semibold">Home</a>
            <a href="/about" className="nav-link uppercase font-semibold">About</a>
            <a href="/service" className="nav-link uppercase font-semibold">Service</a>
            <a href="/product" className="nav-link uppercase font-semibold">Product</a>
            <div className="nav-item">
              <a href="#" className="nav-link uppercase font-semibold">Pages</a>
              <div className="m-0 p-5 hidden bg-bg-color">
                <a href="/blog" className="text-font-color">Blog Grid</a>
                <a href="/detail" className="text-font-color">Blog Detail</a>
                <a href="/feature" className="text-font-color">Features</a>
                <a href="/team" className="text-font-color">The Team</a>
                <a href="/testimonial" className="text-font-color">Testimonial</a>
              </div>
            </div>
            <a href="/contact" className="nav-link uppercase font-semibold">Contact</a>
          </div>
        </div>
      </nav>
    </>
  )
}

export default Header