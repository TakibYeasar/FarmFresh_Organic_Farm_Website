import React from 'react';
import { FaEnvelope, FaPhone, FaTwitter, FaFacebook, FaInstagram, FaLinkedinIn, FaArrowRight } from "react-icons/fa";
import Image from 'next/image';
import footer from "../../assets/img/footer.png";

const Footer = () => {
  return (
    <div className="relative">
      <div className="bg-primary-color">
        <Image className="h-[60vh]" src={footer} alt="" />
      </div>
      <div className='container absolute top-0 left-0 p-28'>
        <div className="grid grid-flow-col justify-between">
          <div className="col-lg-8 justify-between">
            <div className="grid grid-flow-col">
              <div className="col-span-4 pt-5 mb-5">
                <h4 className="text-font-light mb-4">Get In Touch</h4>
                <div className="flex mb-2">
                  <i className="bi bi-geo-alt text-font-light me-2"></i>
                  <p className="text-font-light mb-0">123 Street, New York, USA</p>
                </div>
                <div className="flex mb-2">
                  <FaEnvelope />
                  <p className="text-font-light mb-0">info@example.com</p>
                </div>
                <div className="flex mb-2">
                  <FaPhone />
                  <p className="text-font-light mb-0">+012 345 67890</p>
                </div>
                <div className="flex mt-4">
                  <a className="me-2" href="#"><FaTwitter className="text-4xl text-font-light bg-secondary-color rounded-full p-2" /></a>
                  <a className="me-2" href="#"><FaFacebook className="text-4xl text-font-light bg-secondary-color rounded-full p-2" /></a>
                  <a className="me-2" href="#"><FaLinkedinIn className="text-4xl text-font-light bg-secondary-color rounded-full p-2" /></a>
                  <a className="me-2" href="#"><FaInstagram className="text-4xl text-font-light bg-secondary-color rounded-full p-2" /></a>
                </div>
              </div>
              <div className="col-span-4 pt-0 pt-lg-5 mb-5">
                <h4 className="text-font-light mb-4">Quick Links</h4>
                <div className="grid justify-start">
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Home</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />About Us</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Our Services</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Meet The Team</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Latest Blog</a>
                  <a className="text-font-light" href="#"><FaArrowRight className="text-font-light me-2" />Contact Us</a>
                </div>
              </div>
              <div className="col-span-4 pt-0 pt-lg-5 mb-5">
                <h4 className="text-font-light mb-4">Popular Links</h4>
                <div className="grid justify-start">
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Home</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />About Us</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Our Services</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Meet The Team</a>
                  <a className="text-font-light flex mb-2" href="#"><FaArrowRight className="text-font-light me-2" />Latest Blog</a>
                  <a className="text-font-light flex" href="#"><FaArrowRight className="text-font-light me-2" />Contact Us</a>
                </div>
              </div>
            </div>
          </div>
          <div className="col-span-4 bg-secondary-color h-full">
            <div className="grid text-center p-5 items-center">
              <h4 className="text-font-light">Newsletter</h4>
              <h6 className="text-font-light">Subscribe Our Newsletter</h6>
              <p>Amet justo diam dolor rebum lorem sit stet sea justo kasd</p>
              <form action="">
                <div className="">
                  <input type="text" className="form-control border-font-light p-3" placeholder="Your Email" />
                  <button className="btn-primary hover:bg-green-500">Sign Up</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div className="bg-tertiary-color text-font-light py-4 text-center">
        <p className="my-2 text-xl font-normal text-font-light">&copy; <a className="text-secondary-color" href="#">Your Site Name</a>. All Rights Reserved. Designed by <a className="text-secondary-color" href="https://htmlcodex.com">HTML Codex</a></p>
      </div>
    </div>
  )
}

export default Footer