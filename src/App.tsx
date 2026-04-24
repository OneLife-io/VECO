import Announcement from './components/Announcement'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import LogoMarquee from './components/LogoMarquee'
import Pillars from './components/Pillars'
import AIFeatures from './components/AIFeatures'
import Workloads from './components/Workloads'
import Postgres from './components/Postgres'
import Ecosystem from './components/Ecosystem'
import Stats from './components/Stats'
import CTA from './components/CTA'
import Footer from './components/Footer'

export default function App() {
  return (
    <div className="min-h-screen bg-ink-950 text-white">
      <Announcement />
      <Navbar />
      <main>
        <Hero />
        <LogoMarquee />
        <Pillars />
        <AIFeatures />
        <Workloads />
        <Postgres />
        <Stats />
        <Ecosystem />
        <CTA />
      </main>
      <Footer />
    </div>
  )
}
