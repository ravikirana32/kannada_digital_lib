const jwt=require("jsonwebtoken"); const bcrypt=require("bcryptjs");
const SECRET=process.env.JWT_SECRET||"development-only-change-me";
function sign(user){return jwt.sign({sub:user.id,email:user.email,role:user.role},SECRET,{expiresIn:process.env.JWT_EXPIRES_IN||"8h"})}
function authenticate(req,res,next){const h=req.headers.authorization||"";if(!h.startsWith("Bearer "))return res.status(401).json({error:"authentication_required"});try{req.user=jwt.verify(h.slice(7),SECRET);next()}catch(e){return res.status(401).json({error:"invalid_token"})}}
async function hashPassword(password){return bcrypt.hash(password,12)}
async function verifyPassword(password,hash){return bcrypt.compare(password,hash)}
module.exports={sign,authenticate,hashPassword,verifyPassword};
