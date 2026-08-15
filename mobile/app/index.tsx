import { Link } from "expo-router";
import { View, Text, Pressable, StyleSheet } from "react-native";
export default function Home(){
 return <View style={styles.container}>
   <Text style={styles.title}>ಸರ್ವಜ್ಞ ಡಿಜಿಟಲ್ ಗ್ರಂಥಾಲಯ</Text>
   <Text style={styles.sub}>ಮೂಲ ವಚನ • ಭಾವಾರ್ಥ • ಮೂಲಾಧಾರ</Text>
   <Link href="/tripadi" asChild><Pressable style={styles.button}><Text style={styles.buttonText}>ತ್ರಿಪದಿಗಳು</Text></Pressable></Link>
   <Link href="/search" asChild><Pressable style={styles.button}><Text style={styles.buttonText}>ಹುಡುಕಿ</Text></Pressable></Link>
 <Link href="/compare" asChild><Pressable style={styles.button}><Text style={styles.buttonText}>ಮೂಲಾಧಾರ ಹೋಲಿಕೆ</Text></Pressable></Link></View>
}
const styles=StyleSheet.create({container:{flex:1,padding:24,justifyContent:"center"},title:{fontSize:26,fontWeight:"700",marginBottom:8},sub:{fontSize:16,marginBottom:24},button:{padding:16,borderWidth:1,borderRadius:12,marginBottom:12},buttonText:{fontSize:18}})
