import React,{useMemo,useState} from "react";
import "./styles.css";
const demo=[
 {id:"CAND-0001",section:"ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ",status:"ಪರಿಶೀಲನೆ ಬಾಕಿ",text:"ಮೂಲ ಪಠ್ಯವನ್ನು ಐತಿಹಾಸಿಕ ಮೂಲಗಳೊಂದಿಗೆ ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ.",meaning:"ಭಾವಾರ್ಥವನ್ನು ಮೂಲ ಪಠ್ಯ ಅನುಮೋದನೆಯ ನಂತರ ಸೇರಿಸಲಾಗುತ್ತದೆ."},
 {id:"CAND-0046",section:"ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ",status:"ಪುನರ್‌ಪರಿಶೀಲನೆ",text:"ಮೂಲಾಧಾರ ಲಭ್ಯವಿದೆ; 46–47 ಹೋಲಿಕೆ ನಡೆಯುತ್ತಿದೆ.",meaning:"ಭಾವಾರ್ಥ ಬಾಕಿ."},
 {id:"CAND-0061",section:"ಲಿಂಗಾತಿಶಯ ಪದ್ಧತಿ",status:"ಪುನರ್‌ಪರಿಶೀಲನೆ",text:"61ನೇ ದಾಖಲೆಯಿಂದ ವಿಭಾಗ ಬದಲಾಗುತ್ತದೆ.",meaning:"ಭಾವಾರ್ಥ ಬಾಕಿ."}
];
export default function App(){
 const [q,setQ]=useState(""),[r,setR]=useState(null);
 const list=useMemo(()=>demo.filter(x=>(x.id+x.section+x.text).toLowerCase().includes(q.toLowerCase())),[q]);
 return <div className="site"><header><h1>ಸರ್ವಜ್ಞ ಡಿಜಿಟಲ್ ಗ್ರಂಥಾಲಯ</h1><p>ಮೂಲ ವಚನ • ಭಾವಾರ್ಥ • ಮೂಲಾಧಾರ</p></header>
 <div className="search"><input value={q} onChange={e=>setQ(e.target.value)} placeholder="ತ್ರಿಪದಿ / ಪದ ಹುಡುಕಿ"/></div>
 <div className="content"><nav><h3>ತ್ರಿಪದಿಗಳು</h3>{list.map(x=><button onClick={()=>setR(x)}>{x.id} · {x.section}</button>)}</nav>
 <article>{r?<><div className="badge">{r.status}</div><h2>{r.id}</h2><h3>ಮೂಲ ಕನ್ನಡ</h3><p className="original">{r.text}</p><h3>ಭಾವಾರ್ಥ</h3><p>{r.meaning}</p><h3>ಮೂಲಾಧಾರ</h3><p>Source and historical verification details will appear here after editorial approval.</p></>:<><h2>ಸ್ವಾಗತ</h2><p>ಒಂದು ತ್ರಿಪದಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.</p></>}</article></div>
 </div>
}