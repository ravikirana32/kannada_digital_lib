import { View, Text, TextInput, Pressable, StyleSheet, ScrollView } from "react-native";
import { useState } from "react";
export default function Compare(){
 const [decision,setDecision]=useState("pending");
 return <ScrollView contentContainerStyle={s.c}>
  <Text style={s.h}>ಮೂಲಾಧಾರ ಹೋಲಿಕೆ</Text>
  <Text style={s.id}>CAND-0046</Text>
  <View style={s.card}><Text style={s.label}>ಮೂಲ A</Text><Text>Source reading will appear here.</Text></View>
  <View style={s.card}><Text style={s.label}>ಮೂಲ B</Text><Text>Independent source reading will appear here.</Text></View>
  <Text style={s.label}>ತೀರ್ಮಾನ</Text>
  {["same_text","minor_variant","major_variant","different_poem","needs_historical_check"].map(x=><Pressable onPress={()=>setDecision(x)} style={s.btn}><Text>{x}</Text></Pressable>)}
  <Text>Current: {decision}</Text>
  <TextInput style={s.input} placeholder="Canonical candidate — only after evidence review"/>
 </ScrollView>
}
const s=StyleSheet.create({c:{padding:20},h:{fontSize:26,fontWeight:"700",marginBottom:8},id:{fontSize:18,marginBottom:16},card:{padding:16,borderWidth:1,borderRadius:12,marginBottom:12},label:{fontWeight:"700",marginBottom:8},btn:{padding:12,borderWidth:1,borderRadius:9,marginBottom:8},input:{borderWidth:1,borderRadius:9,padding:12,minHeight:100}})
