import React from 'react';
import Image from 'next/image';
import test01 from "../../assets/img/testimonial-1.jpg";
import test02 from "../../assets/img/testimonial-2.jpg";

const Testimonial = () => {
  return (
    <div className="container">
      <div className="grid justify-center">
        <div className="col-span-7">
          <div className="p-5">
            <div className="text-center text-font-light">
              <Image className="mx-auto p-2 rounded mb-4" src={test01} alt="" />
              <p className="">Dolores sed duo clita justo dolor et stet lorem kasd dolore lorem ipsum. At lorem lorem magna ut et, nonumy labore diam erat. Erat dolor rebum sit ipsum.</p>
              <hr className="mx-auto" />
              <h4 className="text-font-light mb-0">Client Name</h4>
            </div>
            {/* <div className="text-center text-font-light">
              <Image className="mx-auto p-2 rounded mb-4" src={test02} alt="" />
              <p className="">Dolores sed duo clita justo dolor et stet lorem kasd dolore lorem ipsum. At lorem lorem magna ut et, nonumy labore diam erat. Erat dolor rebum sit ipsum.</p>
              <hr className="mx-auto" />
              <h4 className="text-font-light mb-0">Client Name</h4>
            </div> */}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Testimonial