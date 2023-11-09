import React from 'react';
import { FaCarrot } from 'react-icons/fa';

const data = [
  {
    title: "Fresh Vegetables",
    dest: "Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero",
  },
  {
    title: "Fresh Fruits",
    dest: "Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero",
  },
  {
    title: "Healty Cattle",
    dest: "Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero",
  },
  {
    title: "Modern Truck",
    dest: "Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero",
  },
  {
    title: "Farming Plans",
    dest: "Labore justo vero ipsum sit clita erat lorem magna clita nonumy dolor magna dolor vero",
  },
]

const Services = () => {
  return (
    <div className="container">
      <div className="grid grid-flow-col">

        <div className="col-span-4">
          <div className="mb-3">
            <h6 className="uppercase">Services</h6>
            <h1 className="">Organic Farm Services</h1>
          </div>
          <p className="mb-4">Tempor erat elitr at rebum at at clita. Diam dolor diam ipsum et tempor sit. Clita erat ipsum et lorem et sit sed stet labore</p>
          <a href="" className="btn-style">Contact Us</a>
        </div>

        <div className="grid grid-flow-col">
          {data.map((item, i) => (
            <div className="col-span-4 bg-green-200" key={i}>
              <div className="text-center p-5">
                <h4>{item?.title}</h4>
                <p className="mb-0">{item?.dest}</p>
              </div>
            </div>
          ))}
        </div>


      </div>
    </div>
  )
}

export default Services