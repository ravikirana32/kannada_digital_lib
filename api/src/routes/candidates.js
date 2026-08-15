const express=require("express");const {Candidate,Decision}=require("../models");const {authenticate}=require("../auth/auth");const {requirePermission}=require("../auth/rbac");
const router=express.Router();
router.use(authenticate);
router.get("/",requirePermission("candidate:read"),async(req,res)=>{const where=req.query.q?{section:req.query.q}:{};res.json(await Candidate.findAll({where,order:[["source_number","ASC"]]}))});
router.get("/:id",requirePermission("candidate:read"),async(req,res)=>{const r=await Candidate.findByPk(req.params.id);if(!r)return res.status(404).json({error:"not_found"});res.json(r)});
router.post("/:id/decision",requirePermission("comparison:approve"),async(req,res)=>{const {decision,note}=req.body||{};const allowed=["same_text","minor_variant","major_variant","different_poem","needs_historical_check","needs_revision","approved","rejected"];if(!allowed.includes(decision))return res.status(400).json({error:"invalid_decision"});const item=await Decision.create({candidate_id:req.params.id,decision,note:note||""});res.status(201).json(item)});
module.exports=router;
