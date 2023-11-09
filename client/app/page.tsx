import { About, Banner, Blog, Features, Products, Service, Team, Testimonial } from '@/containers'
import Image from 'next/image'

export default function Home() {
  return (
    <>
      <Banner />
      <About />
      <Service />
      <Features />
      <Products />
      <Testimonial />
      <Team />
      <Blog />
    </>
  )
}
