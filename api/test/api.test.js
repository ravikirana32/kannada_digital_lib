const test=require("node:test");
const assert=require("node:assert/strict");
test("publication gate requires all gates",async()=>{
 const r=await fetch("http://localhost:4000/api/publication/check",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({original_kannada:"x",bhavartha:"y",gates:{historical:true,authenticity:true,rights:true,editorial:false}})});
 const d=await r.json(); assert.equal(d.publishable,false);
});
