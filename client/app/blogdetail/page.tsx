import React from 'react';
import Image from 'next/image';
import blog01 from "../../assets/img/blog-1.jpg";
import blog02 from "../../assets/img/blog-2.jpg";
import blog03 from "../../assets/img/blog-3.jpg";
import user from "../../assets/img/user.jpg";
import { FaArrowRight, FaSearch } from 'react-icons/fa';
import { Blogtags, Categories, Recentpost } from '@/containers';

const page = () => {
  return (
    <div className='container'>
      <div className="grid justify-start">
        <div className="col-span-8 text-center">
          <h1 className=" text-font-light">Blog Detail</h1>
          <a href="" className="me-3">Home</a>
          <a href="" className="">Blog Detail</a>
        </div>
      </div>

      <div className="grid">
        <div className="col-span-8">
          <div className="mb-5">
            <div className="grid mb-5">
              <div className="col-span-6">
                <Image className="w-100" src={blog01} alt="" />
              </div>
              <div className="col-span-6">
                <Image className="w-100" src={blog02} alt="" />
              </div>
            </div>
            <h1 className="mb-4">Diam dolor est labore duo ipsum clita sed et lorem tempor duo</h1>
            <p>Sadipscing labore amet rebum est et justo gubergren. Et eirmod ipsum sit diam ut
              magna lorem. Nonumy vero labore lorem sanctus rebum et lorem magna kasd, stet
              amet magna accusam consetetur eirmod. Kasd accusam sit ipsum sadipscing et at at
              sanctus et. Ipsum sit gubergren dolores et, consetetur justo invidunt at et
              aliquyam ut et vero clita. Diam sea sea no sed dolores diam nonumy, gubergren
              sit stet no diam kasd vero.</p>
            <p>Voluptua est takimata stet invidunt sed rebum nonumy stet, clita aliquyam dolores
              vero stet consetetur elitr takimata rebum sanctus. Sit sed accusam stet sit
              nonumy kasd diam dolores, sanctus lorem kasd duo dolor dolor vero sit et. Labore
              ipsum duo sanctus amet eos et. Consetetur no sed et aliquyam ipsum justo et,
              clita lorem sit vero amet amet est dolor elitr, stet et no diam sit. Dolor erat
              justo dolore sit invidunt.</p>
            <p>Diam dolor est labore duo invidunt ipsum clita et, sed et lorem voluptua tempor
              invidunt at est sanctus sanctus. Clita dolores sit kasd diam takimata justo diam
              lorem sed. Magna amet sed rebum eos. Clita no magna no dolor erat diam tempor
              rebum consetetur, sanctus labore sed nonumy diam lorem amet eirmod. No at tempor
              sea diam kasd, takimata ea nonumy elitr sadipscing gubergren erat. Gubergren at
              lorem invidunt sadipscing rebum sit amet ut ut, voluptua diam dolores at
              sadipscing stet. Clita dolor amet dolor ipsum vero ea ea eos.</p>
          </div>

          <div className="mb-5">
            <h2 className="mb-4">3 Comments</h2>
            <div className="flex mb-4">
              <Image src={user} className="" alt='' />
              <div className="ps-3">
                <h6><a href="">John Doe</a> <small><i>01 Jan 2045</i></small></h6>
                <p>Diam amet duo labore stet elitr invidunt ea clita ipsum voluptua, tempor labore
                  accusam ipsum et no at. Kasd diam tempor rebum magna dolores sed eirmod</p>
                <button className="btn-style">Reply</button>
              </div>
            </div>
            <div className="flex mb-4">
              <Image src={user} className="" alt='' />
              <div className="ps-3">
                <h6><a href="">John Doe</a> <small><i>01 Jan 2045</i></small></h6>
                <p>Diam amet duo labore stet elitr invidunt ea clita ipsum voluptua, tempor labore
                  accusam ipsum et no at. Kasd diam tempor rebum magna dolores sed eirmod</p>
                <button className="btn-style">Reply</button>
              </div>
            </div>
            <div className="flex ms-5 mb-4">
              <Image src={user} className="" alt='' />
              <div className="ps-3">
                <h6><a href="">John Doe</a> <small><i>01 Jan 2045</i></small></h6>
                <p>Diam amet duo labore stet elitr invidunt ea clita ipsum voluptua, tempor labore
                  accusam ipsum et no at. Kasd diam tempor rebum magna dolores sed eirmod</p>
                <button className="btn-style">Reply</button>
              </div>
            </div>
          </div>

          <div className="p-5">
            <h2 className="text-font-light mb-4">Leave a comment</h2>
            <form>
              <div className="grid">
                <div className="col-span-12">
                  <input type="text" className="bg-bg-color border-0" placeholder="Your Name" />
                </div>
                <div className="col-span-12">
                  <input type="email" className="bg-bg-color border-0" placeholder="Your Email" />
                </div>
                <div className="col-span-12">
                  <input type="text" className="bg-bg-color border-0" placeholder="Website" />
                </div>
                <div className="col-span-12">
                  <textarea className="bg-bg-color border-0" placeholder="Comment"></textarea>
                </div>
                <div className="col-span-12">
                  <button className="w-100 py-3" type="submit">Leave Your Comment</button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div className="col-span-4">
          <div className="mb-5">
            <div className="">
              <input type="text" className="p-3" placeholder="Keyword" />
              <button className="px-4"><FaSearch /></button>
            </div>
          </div>

          <Categories />

          <Recentpost />

          <div className="mb-5">
            <Image src={blog01} alt="" className="rounded" />
          </div>

          <Blogtags />

          <div>
            <h2 className="mb-4">Plain Text</h2>
            <div className="text-center text-font-light" >
              <p>Vero sea et accusam justo dolor accusam lorem consetetur, dolores sit amet sit dolor clita kasd justo, diam accusam no sea ut tempor magna takimata, amet sit et diam dolor ipsum amet diam</p>
              <a href="" className="btn-style">Read More</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default page