import { Features } from '@/containers';
import React from 'react';
import Image from 'next/image';
import product01 from "../../assets/img/product-1.png";
import product02 from "../../assets/img/product-2.png";
import product03 from "../../assets/img/product-3.png";
import product04 from "../../assets/img/product-4.png";
import product05 from "../../assets/img/product-5.png";
import { FaCarAlt, FaEye } from 'react-icons/fa';

const proddata = [
    {
        image: product01,
    },
    {
        image: product02,
    },
    {
        image: product03,
    },
    {
        image: product04,
    },
    {
        image: product05,
    },
]

const page = () => {
    return (
        <div className='container'>
            <div className="row justify-start">
                <div className="col-span-8 text-center">
                    <h1 className="text-font-light">Our Products</h1>
                    <a href="" className="me-3">Home</a>
                    <a href="" className="">Products</a>
                </div>
            </div>

            <div className="container">
                <div className="mx-auto text-center mb-5" >
                    <h6 className="uppercase">Products</h6>
                    <h1 className="">Our Fresh & Organic Products</h1>
                </div>
                <div className="px-5">

                    {proddata.map((item, i) => (
                        <div className="pb-5" key={i}>
                            <div className="relative bg-bg-color d-flex text-center">
                                <Image className="mb-4" src={item?.image} alt="" />
                                <h6 className="mb-3">Organic Vegetable</h6>
                                <h5 className="mb-0">$19.00</h5>
                                <div className="flex justify-center">
                                    <a className="py-2 px-3" href=""><FaCarAlt /></a>
                                    <a className="py-2 px-3" href=""><FaEye /></a>
                                </div>
                            </div>
                        </div>
                    ))}

                    
                </div>
            </div>

            <Features />
        </div>
    )
}

export default page