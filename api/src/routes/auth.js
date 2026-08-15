const express=require("express");const fs=require("fs");const path=require("path");const {sign,verifyPassword}=require("../auth/auth");
const router=express.Router();const file=path.join(__dirname,"../auth/users.json");
router.post("/login",async(req,res)=>{const {email,password}=req.body||{};const users=JSON.parse(fs.readFileSync(file,"utf8")).users;const u=users.find(x=>x.email.toLowerCase()===String(email||"").toLowerCase());if(!u||!(await verifyPassword(password||"",u.password_hash)))return res.status(401).json({error:"invalid_credentials"});res.json({token:sign({id:u.id,email:u.email,role:u.role}),user:{id:u.id,email:u.email,role:u.role}})});
module.exports=router;
