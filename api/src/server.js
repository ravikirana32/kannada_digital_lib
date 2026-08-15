require("dotenv").config(); const express=require("express"); const cors=require("cors");
const candidates=require("./routes/candidates"), comparisons=require("./routes/comparisons"), publication=require("./routes/publication"), auth=require("./routes/auth");
const app=express(); app.use(cors()); app.use(express.json({limit:"2mb"}));
app.get("/health",(req,res)=>res.json({status:"ok",service:"sarvajna-api",version:"0.1.0"}));
app.use("/api/auth",auth); app.use("/api/candidates",candidates); app.use("/api/comparisons",comparisons); app.use("/api/publication",publication);
app.use((err,req,res,next)=>{console.error(err);res.status(500).json({error:"internal_error"})});
const port=process.env.PORT||4000; app.listen(port,()=>console.log(`Sarvajna API listening on ${port}`));
module.exports=app;
