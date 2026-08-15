const fs=require("fs");
const path=require("path");
const file=path.join(__dirname,"db.json");
function read(){return JSON.parse(fs.readFileSync(file,"utf8"))}
function write(d){fs.writeFileSync(file,JSON.stringify(d,null,2),"utf8")}
function all(type){return read()[type]||[]}
function add(type,item){const d=read(); d[type]=d[type]||[]; d[type].push(item); write(d); return item}
function update(type,id,patch){const d=read(); const i=(d[type]||[]).findIndex(x=>x.id===id||x.candidate_id===id); if(i<0)return null; d[type][i]={...d[type][i],...patch,updated_at:new Date().toISOString()}; write(d); return d[type][i]}
module.exports={read,write,all,add,update};
