import {Routes, Route, Link, useParams, useSearchParams} from 'react-router-dom'
import {useMemo, useState} from 'react'
import demo from './data/demo-tripadi.json'

const categories=['ಎಲ್ಲ','ಸತ್ಯ','ಧರ್ಮ','ಜ್ಞಾನ','ನೀತಿ','ಭಕ್ತಿ','ಸಮಾಜ','ಆತ್ಮಜ್ಞಾನ']

function Layout({children}) {
  return <div className="site">
    <header className="topbar">
      <Link to="/" className="brand">ಕನ್ನಡ ಡಿಜಿಟಲ್ ಲೈಬ್ರರಿ</Link>
      <nav><Link to="/sarvajna">ಸರ್ವಜ್ಞ</Link><Link to="/categories">ವರ್ಗಗಳು</Link><Link to="/about">ನಮ್ಮ ಬಗ್ಗೆ</Link></nav>
    </header>
    {children}
    <footer>Kannada Digital Library · Phase 3 · Content is added only after source verification.</footer>
  </div>
}

function Home(){
  return <Layout><main className="container">
    <section className="hero"><span>ಕನ್ನಡ ಜ್ಞಾನಸಂಪದ</span><h1>ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು</h1><p>ಮೂಲ ಕನ್ನಡ · ಭಾವಾರ್ಥ · ಜೀವನ ಸಂದೇಶ</p>
    <Link className="primary" to="/sarvajna">ಸರ್ವಜ್ಞ ತ್ರಿಪದಿಗಳಿಗೆ ಹೋಗಿ →</Link></section>
    <section className="grid3"><div><b>📚</b><h3>ಪುಸ್ತಕ</h3><p>ಒಂದೇ data source ನಿಂದ ಪುಸ್ತಕ ರೂಪಗಳು.</p></div><div><b>🔎</b><h3>ಹುಡುಕಾಟ</h3><p>ತ್ರಿಪದಿ, ಭಾವಾರ್ಥ, ವರ್ಗ ಮತ್ತು keywords ಮೂಲಕ ಹುಡುಕಿ.</p></div><div><b>🎥</b><h3>ಡಿಜಿಟಲ್ ವಿಷಯ</h3><p>YouTube ಮತ್ತು Instagramಗೆ ಸಿದ್ಧವಾಗುವ metadata.</p></div></section>
  </main></Layout>
}

function Sarvajna(){
  const [q,setQ]=useState(''); const [cat,setCat]=useState('ಎಲ್ಲ')
  const items=[demo]
  const filtered=useMemo(()=>items.filter(x=>{
    const t=[x.original,x.bhavartha,x.life_message,x.category,...x.keywords].join(' ').toLowerCase()
    return (!q || t.includes(q.toLowerCase())) && (cat==='ಎಲ್ಲ'||x.category===cat)
  }),[q,cat])
  return <Layout><main className="container"><div className="pagehead"><span>BOOK 1</span><h1>ಸರ್ವಜ್ಞ ತ್ರಿಪದಿಗಳು</h1><p>ಈಗ UI demo ಮಾತ್ರ. ಪರಿಶೀಲಿತ ಮೂಲ ಪಠ್ಯವನ್ನು ಹಂತ ಹಂತವಾಗಿ ಸೇರಿಸಲಾಗುತ್ತದೆ.</p></div>
  <input className="search" value={q} onChange={e=>setQ(e.target.value)} placeholder="ತ್ರಿಪದಿ, ಭಾವಾರ್ಥ ಅಥವಾ ಪದ ಹುಡುಕಿ..."/>
  <div className="chips">{categories.map(c=><button className={cat===c?'active':''} onClick={()=>setCat(c)} key={c}>{c}</button>)}</div>
  <div className="cards">{filtered.map(x=><TripadiCard x={x} key={x.id}/>)}</div></main></Layout>
}

function TripadiCard({x}){
  return <article className="card"><div className="badge">DEMO / PLACEHOLDER</div><h2>ತ್ರಿಪದಿ UI Preview</h2><blockquote>{x.original}</blockquote><h4>ಭಾವಾರ್ಥ</h4><p>{x.bhavartha}</p><h4>ಜೀವನ ಸಂದೇಶ</h4><p>{x.life_message}</p><div className="meta">ವರ್ಗ: {x.category}</div><Link to="/sarvajna/SAR-DEMO-0001">ವಿವರ ನೋಡಿ →</Link></article>
}

function Detail(){
  const {id}=useParams()
  return <Layout><main className="container narrow"><div className="pagehead"><span>{id}</span><h1>ತ್ರಿಪದಿ ವಿವರ</h1></div><article className="card"><div className="badge">DEMO / PLACEHOLDER</div><blockquote>{demo.original}</blockquote><h3>ಭಾವಾರ್ಥ</h3><p>{demo.bhavartha}</p><h3>ಜೀವನ ಸಂದೇಶ</h3><p>{demo.life_message}</p><h3>ಮೂಲ</h3><p>{demo.source.title} — {demo.source.notes}</p></article></main></Layout>
}

function Categories(){
 return <Layout><main className="container"><div className="pagehead"><span>EXPLORE</span><h1>ವಿಷಯವಾರು ವರ್ಗಗಳು</h1></div><div className="categorygrid">{categories.filter(x=>x!=='ಎಲ್ಲ').map(c=><Link to={`/sarvajna?category=${encodeURIComponent(c)}`} className="category" key={c}>{c}<span>→</span></Link>)}</div></main></Layout>
}

function About(){
 return <Layout><main className="container narrow"><div className="pagehead"><span>PROJECT</span><h1>ಕನ್ನಡ ಡಿಜಿಟಲ್ ಲೈಬ್ರರಿ</h1></div><article className="card"><p>ಕನ್ನಡದ ಶ್ರೇಷ್ಠ ಜ್ಞಾನ ಸಾಹಿತ್ಯವನ್ನು ವಿಶ್ವಾಸಾರ್ಹ, ಹುಡುಕಬಹುದಾದ ಮತ್ತು ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ಡಿಜಿಟಲ್ ರೂಪದಲ್ಲಿ ಸಂರಕ್ಷಿಸುವುದು ಈ ಯೋಜನೆಯ ಉದ್ದೇಶ.</p><p>ಸರ್ವಜ್ಞ ತ್ರಿಪದಿಗಳು ಮೊದಲ ಗ್ರಂಥ. ಮೂಲ ಪಠ್ಯಕ್ಕೆ source verification ಮತ್ತು rights tracking ಕಡ್ಡಾಯ.</p></article></main></Layout>
}

export default function App(){
 return <Routes><Route path="/" element={<Home/>}/><Route path="/sarvajna" element={<Sarvajna/>}/><Route path="/sarvajna/:id" element={<Detail/>}/><Route path="/categories" element={<Categories/>}/><Route path="/about" element={<About/>}/></Routes>
}
