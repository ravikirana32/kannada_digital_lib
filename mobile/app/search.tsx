import { View, TextInput, Text, StyleSheet } from "react-native";
export default function Search(){return <View style={s.c}><Text style={s.h}>ಹುಡುಕಿ</Text><TextInput placeholder="ಪದ ಅಥವಾ ತ್ರಿಪದಿ ಹುಡುಕಿ" style={s.input}/><Text>Search API will connect to the canonical corpus.</Text></View>}
const s=StyleSheet.create({c:{flex:1,padding:24},h:{fontSize:26,fontWeight:"700",marginBottom:16},input:{borderWidth:1,borderRadius:10,padding:12,marginBottom:16}})
