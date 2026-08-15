const permissions={
 researcher:["candidate:read","source:read","comparison:create","comparison:read"],
 reviewer:["candidate:read","source:read","comparison:create","comparison:read","comparison:approve"],
 editor:["candidate:read","source:read","comparison:read","comparison:approve","bhavartha:approve","canonical:approve","publication:approve"],
 admin:["*"]
};
function hasPermission(role,permission){return permissions[role]?.includes("*")||permissions[role]?.includes(permission)}
function requirePermission(permission){return (req,res,next)=>{if(!req.user)return res.status(401).json({error:"authentication_required"});if(!hasPermission(req.user.role,permission))return res.status(403).json({error:"forbidden",permission});next()}}
module.exports={permissions,hasPermission,requirePermission};
