import React,{useMemo,useState} from "react";
import {createRoot} from "react-dom/client";
import "./styles.css";

const candidates=[
 {id:"CAND-0001",section:"ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ",a:"Wikisource reading available",b:"Independent source reading pending",status:"historical_review",decision:"pending"},
 {id:"CAND-0046",section:"ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ",a:"Source reading 46",b:"Source reading 46/47 comparison required",status:"reconciliation_pending",decision:"pending"},
 {id:"CAND-0047",section:"ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ",a:"Source reading 47",b:"Source reading 46/47 comparison required",status:"reconciliation_pending",decision:"pending"},
 {id:"CAND-0061",section:"ಲಿಂಗಾತಿಶಯ ಪದ್ಧತಿ",a:"Source reading 61",b:"Independent source reading pending",status:"reconciliation_pending",decision:"pending"}
];

function App(){
 const [rows,setRows]=useState(candidates),[q,setQ]=useState(""),[sel,setSel]=useState(candidates[1]);
 const filtered=useMemo(()=>rows.filter(r=>(r.id+r.section+r.status).toLowerCase().includes(q.toLowerCase())),[q]);
 const choose=(decision)=>setRows(rs=>rs.map(r=>r.id===sel.id?{...r,decision}:r));
 return <main>
  <header><div><h1>ಸರ್ವಜ್ಞ — Source Comparison</h1><p>Compare source readings before canonical approval</p></div><div className="gate">Canonical approvals: <b>0</b></div></header>
  <div className="toolbar"><input value={q} onChange={e=>setQ(e.target.value)} placeholder="Candidate / section / status ಹುಡುಕಿ"/></div>
  <div className="layout">
   <aside><h2>Review Queue</h2>{filtered.map(r=><button className={r.id===sel.id?"item selected":"item"} onClick={()=>setSel(r)} key={r.id}>
    <b>{r.id}</b><span>{r.section}</span><small>{r.status}</small></button>)}</aside>
   <section className="review">
    <div className="reviewHead"><div><h2>{sel.id}</h2><span className="pill">{sel.status}</span></div><span>Decision: <b>{sel.decision}</b></span></div>
    <div className="sources">
      <div className="source"><h3>Source A — Primary candidate</h3><p>{sel.a}</p><label>Source / locator</label><input placeholder="Edition, page or URL"/></div>
      <div className="source"><h3>Source B — Comparison</h3><p>{sel.b}</p><label>Source / locator</label><input placeholder="Edition, page or URL"/></div>
    </div>
    <div className="decision"><h3>Reconciliation decision</h3>
      <button onClick={()=>choose("same_text")}>Same text</button>
      <button onClick={()=>choose("minor_variant")}>Minor variant</button>
      <button onClick={()=>choose("major_variant")}>Major variant</button>
      <button onClick={()=>choose("different_poem")}>Different poem</button>
      <button onClick={()=>choose("needs_historical_check")}>Historical check required</button>
    </div>
    <div className="canonical"><h3>Canonical text candidate</h3><textarea placeholder="Enter only after evidence comparison. Do not silently normalize source readings."/>
      <div className="actions"><button onClick={()=>choose("needs_revision")}>Save as draft</button><button className="approve" onClick={()=>choose("approved")}>Approve canonical</button></div>
      <p>Approval should ultimately be enforced by the backend against source, authenticity and rights gates.</p>
    </div>
   </section>
  </div>
 </main>
}
createRoot(document.getElementById("root")).render(<App/>);
