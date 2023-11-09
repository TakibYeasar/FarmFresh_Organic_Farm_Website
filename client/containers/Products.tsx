import React from 'react';
import { FaShoppingCart, FaEye } from "react-icons/fa";
import Image from 'next/image';
import prod01 from "../../assets/img/product-1.png";
import prod02 from "../../assets/img/product-2.png";
import prod03 from "../../assets/img/product-1.png";
import prod04 from "../../assets/img/product-2.png";
import prod05 from "../../assets/img/product-1.png";

const data = [
  {
    image: prod01,
    title: "Organic Vegetable",
    price: "$19.00",
  },
  {
    image: prod02,
    title: "Organic Vegetable",
    price: "$19.00",
  },
  {
    image: prod03,
    title: "Organic Vegetable",
    price: "$19.00",
  },
  {
    image: prod04,
    title: "Organic Vegetable",
    price: "$19.00",
  },
  {
    image: prod05,
    title: "Organic Vegetable",
    price: "$19.00",
  },
]

const Products = () => {
  return (
    <div className="container">
      <div className="mx-auto text-center mb-5" >
        <h6 className="uppercase">Products</h6>
        <h1 className="">Our Fresh & Organic Products</h1>
      </div>
      <div className="grid grid-flow-col gap-4">

        {data.map((item, i) => (
          <div className="relative bg-bg-color flex text-center" key={i}>
            <Image className="mb-4" src={item?.image} alt="" />
            <h6 className="mb-3">{item?.title}</h6>
            <h5 className="mb-0">{item?.price}</h5>
            <div className="flex justify-center">
              <a className="py-2 px-3" href=""><FaShoppingCart /></a>
              <a className="py-2 px-3" href=""><FaEye /></a>
            </div>
          </div>
        ))}

      </div>
    </div>
  )
}

export default Products