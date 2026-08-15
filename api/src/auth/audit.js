const {AuditLog}=require("../models");
async function audit(action,entityType,getId){return async(req,res,next)=>{try{await AuditLog.create({entity_type:entityType,entity_id:String(getId(req)),action,actor_id:req.user?.sub,before_json:req.auditBefore||null,after_json:req.body||null})}catch(e){console.error("audit failure",e.message)}next()}}
module.exports={audit};
