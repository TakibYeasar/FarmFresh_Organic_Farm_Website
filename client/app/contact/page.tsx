import React from 'react'
import { FaEnvelopeOpen, FaPhone } from 'react-icons/fa'

const page = () => {
  return (
    <div className="container">
      <div className="grid justify-start">
        <div className="col-span-8 text-center">
          <h1 className=" text-font-light">Contact Us</h1>
          <a href="" className="me-3">Home</a>
          <a href="" className="">Contact Us</a>
        </div>
      </div>
      <div className="">
        <div className="mx-auto text-center mb-5" >
          <h6 className="uppercase">Contact Us</h6>
          <h1 className="">Please Feel Free To Contact Us</h1>
        </div>
        <div className="grid ">
          <div className="col-span-7">
            <div className="h-100 p-5">
              <form>
                <div className="grid">
                  <div className="col-span-6">
                    <input type="text" className="border-0 px-4" placeholder="Your Name" />
                  </div>
                  <div className="col-span-6">
                    <input type="email" className="border-0 px-4" placeholder="Your Email" />
                  </div>
                  <div className="col-span-12">
                    <input type="text" className="border-0 px-4" placeholder="Subject" />
                  </div>
                  <div className="col-span-12">
                    <textarea className="border-0 px-4 py-3" placeholder="Message"></textarea>
                  </div>
                  <div className="col-span-12">
                    <button className="btn-style" type="submit">Send Message</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div className="col-span-5">
            <div className="h-100 p-5">
              <h2 className="text-font-light mb-4">Get In Touch</h2>
              <div className="flex mb-4">
                <div className="flex items-center justify-center" />
                <i className="bi bi-geo-alt fs-4 text-font-light"></i>
              </div>
              <div className="ps-3">
                <h5 className="text-font-light">Our Office</h5>
                <span className="text-font-light">123 Street, New York, USA</span>
              </div>
            </div>
            <div className="flex mb-4">
              <div className="flex items-center justify-center" />
              <FaEnvelopeOpen />
            </div>
            <div className="ps-3">
              <h5 className="text-font-light">Email Us</h5>
              <span className="text-font-light">info@example.com</span>
            </div>
          </div>
          <div className="flex">
            <div className="flex items-center justify-center" />
            <FaPhone />
          </div>
          <div className="ps-3">
            <h5 className="text-font-light">Call Us</h5>
            <span className="text-font-light">+012 345 6789</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default page