const express=require("express");const {Candidate}=require("../models");const {authenticate}=require("../auth/auth");const {requirePermission}=require("../auth/rbac");
const router=express.Router();
router.get("/ready",async(req,res)=>res.json(await Candidate.findAll({where:{editorial_status:"approved",publication_ready:true}})));
router.post("/check",authenticate,requirePermission("publication:approve"),async(req,res)=>{const r=req.body||{},g=r.gates||{};const ok=!!(r.original_kannada&&r.bhavartha&&g.historical&&g.authenticity&&g.rights&&g.editorial);res.json({publishable:ok,reason:ok?"all_gates_passed":"publication_gate_not_satisfied"})});
module.exports=router;
