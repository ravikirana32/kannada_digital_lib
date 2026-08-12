import { useMemo, useState } from 'react'
import demo from './data/demo-tripadi.json'

const categories = ['ಎಲ್ಲ','ಸತ್ಯ','ಧರ್ಮ','ಜ್ಞಾನ','ನೀತಿ','ಭಕ್ತಿ','ಸಮಾಜ']

export default function App() {
  const [q,setQ]=useState('')
  const [cat,setCat]=useState('ಎಲ್ಲ')
  const items=[demo]
  const filtered=useMemo(()=>items.filter(x=>{
    const text=[x.original,x.bhavartha,x.life_message,x.category,...x.keywords].join(' ').toLowerCase()
    return (!q || text.includes(q.toLowerCase())) && (cat==='ಎಲ್ಲ' || x.category===cat)
  }),[q,cat])

  return <div className="app">
    <header><div><div className="eyebrow">KANNADA DIGITAL LIBRARY</div><h1>ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು</h1><p>ಮೂಲ ಕನ್ನಡ • ಭಾವಾರ್ಥ • ಜೀವನ ಸಂದೇಶ</p></div></header>
    <main>
      <section className="hero"><h2>ಕನ್ನಡ ಜ್ಞಾನವನ್ನು ಡಿಜಿಟಲ್ ರೂಪದಲ್ಲಿ</h2><p>ಮೂಲ ಪಠ್ಯವನ್ನು ಪರಿಶೀಲಿಸಿ, ಭಾವಾರ್ಥವನ್ನು ಅರ್ಥಮಾಡಿಕೊಂಡು, ಹುಡುಕಬಹುದಾದ ರೂಪದಲ್ಲಿ ಸಂರಕ್ಷಿಸುವ ವೇದಿಕೆ.</p></section>
      <section className="controls">
        <input value={q} onChange={e=>setQ(e.target.value)} placeholder="ತ್ರಿಪದಿ, ಭಾವಾರ್ಥ ಅಥವಾ ಪದ ಹುಡುಕಿ..." />
        <div className="chips">{categories.map(c=><button className={cat===c?'active':''} onClick={()=>setCat(c)} key={c}>{c}</button>)}</div>
      </section>
      <section>{filtered.map(x=><article className="card" key={x.id}>
        <div className="demo">DEMO / CONTENT PLACEHOLDER</div>
        <h3>ತ್ರಿಪದಿ UI Preview</h3>
        <blockquote>{x.original}</blockquote>
        <h4>ಭಾವಾರ್ಥ</h4><p>{x.bhavartha}</p>
        <h4>ಜೀವನ ಸಂದೇಶ</h4><p>{x.life_message}</p>
        <small>ವರ್ಗ: {x.category}</small>
      </article>)}</section>
    </main>
    <footer>Kannada Digital Library · Phase 3 Foundation</footer>
  </div>
}
